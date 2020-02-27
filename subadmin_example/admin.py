from django.contrib import admin
from subadmin import SubAdmin, RootSubAdmin

from .models import MailingList, Subscriber, Message, Attachment


class AttachmentSubAdmin(SubAdmin):
    model = Attachment


class MessageSubAdmin(SubAdmin):
    model = Message
    list_display = ('subject',)
    subadmins = [AttachmentSubAdmin]


class SubscriberSubAdmin(SubAdmin):
    model = Subscriber
    list_display = ('username',)

    subadmins = [MessageSubAdmin]


class MailingListAdmin(RootSubAdmin):
    list_display = ('name',)

    subadmins = [SubscriberSubAdmin, MessageSubAdmin]


admin.site.register(MailingList, MailingListAdmin)