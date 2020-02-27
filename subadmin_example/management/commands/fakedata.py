from django.core.management.base import BaseCommand

from subadmin_example.models import MailingList, Subscriber, Message, Attachment


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1,3):
            ml = MailingList.objects.create(name="Mailing list {0}".format(i))

            for ii in range(1,101):
                sub = Subscriber.objects.create(
                    mailing_list = ml,
                    username = "user{0}".format(ii)
                )

                for iii in range(1, 11):
                    msg = Message.objects.create(
                        mailing_list = ml,
                        subscriber = sub,
                        subject = "Subject {0}".format(iii)
                    )

                    for iiii in range(1,3):
                        att = Attachment.objects.create(
                            message = msg,
                            filename = "filename_{0}.png".format(iiii)
                        )

        self.stdout.write(self.style.SUCCESS('generated some fake data'))