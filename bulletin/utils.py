""" 
Copyright 2016, 2017 UFPE - Universidade Federal de Pernambuco
 
Este arquivo é parte do programa Amadeus Sistema de Gestão de Aprendizagem, ou simplesmente Amadeus LMS
 
O Amadeus LMS é um software livre; você pode redistribui-lo e/ou modifica-lo dentro dos termos da Licença Pública Geral GNU como publicada pela Fundação do Software Livre (FSF); na versão 2 da Licença.
 
Este programa é distribuído na esperança que possa ser útil, mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a Licença Pública Geral GNU para maiores detalhes.
 
Você deve ter recebido uma cópia da Licença Pública Geral GNU, sob o título "LICENSE", junto com este programa, se não, escreva para a Fundação do Software Livre (FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA.
"""

import json
import textwrap

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models import Q
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import formats
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _

from api.utils import send_chat_push_notification
from chat.models import Conversation, TalkMessages, ChatVisualizations


def brodcast_dificulties(request, message, subject):
    msg = TalkMessages()
    msg.text = message
    msg.user = request.user
    msg.subject = subject

    simple_notify = textwrap.shorten(strip_tags(msg.text), width=30, placeholder="...")

    channel_layer = get_channel_layer()

    for p in subject.professor.all():
        talks = Conversation.objects.filter(
            (Q(user_one=request.user) & Q(user_two__email=p.email)) | (
                    Q(user_two=request.user) & Q(user_one__email=p.email)))

        if talks.count() > 0:
            msg.talk = talks[0]
        else:
            msg.talk = Conversation.objects.create(user_one=request.user, user_two=p)

        msg.save()

        notification = {
            "type": "chat",
            "subtype": subject.slug,
            "space": "subject",
            "user_icon": request.user.image_url,
            "notify_title": str(request.user),
            "simple_notify": simple_notify,
            "view_url": reverse("chat:view_message", args=(msg.id,), kwargs={}),
            "complete": render_to_string("chat/_message.html", {"talk_msg": msg}, request),
            "container": "chat-" + str(request.user.id),
            "last_date": _("Last message in %s") % (
                formats.date_format(msg.create_date, "SHORT_DATETIME_FORMAT"))
        }

        notification = json.dumps(notification)
        async_to_sync(channel_layer.send)("user-%s" % p.id, {'text': notification})
        send_chat_push_notification(p, msg)

        ChatVisualizations.objects.create(viewed=False, message=msg, user=p)
