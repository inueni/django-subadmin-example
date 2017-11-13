# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MailingList(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Subscriber(models.Model):
    mailing_list = models.ForeignKey(MailingList)
    username = models.CharField(max_length=100)

    def __unicode__(self):
        return self.username


class Message(models.Model):
    mailing_list = models.ForeignKey(MailingList)
    subscriber = models.ForeignKey(Subscriber)
    subject = models.CharField(max_length=100)

    def __unicode__(self):
        return self.subject


class Attachment(models.Model):
    message = models.ForeignKey(Message)
    filename = models.CharField(max_length=100)

    def __unicode__(self):
        return self.filename