from django.db import models


class MailingList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Message(models.Model):
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject


class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    filename = models.CharField(max_length=100)

    def __str__(self):
        return self.filename