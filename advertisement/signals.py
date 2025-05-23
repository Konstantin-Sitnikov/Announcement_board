from django.contrib.auth.models import Group, User

from django.dispatch import receiver
from django.db.models.signals import post_save
from advertisement.models import Feedback, News
from .tasks import (send_message_feedback_created,
                    send_message_feedback_accepted,
                    send_message_news_created)


@receiver(post_save, sender=Feedback)
def notify_about_new_feedback(sender, instance, **kwargs):
    """
    Сигнал для рассылки сообщений об отклике/принятии отклика
    если параметр instance.feedback_received = False (по умолчанию при создании отклика)
    отправляется сообщение о новом отклике к объявлению.

    Если параметр instance.feedback_received = True (формируется при принятии отклика)
    отправляется сообщение о принятии отклика


    """
    if not instance.feedback_received:
        author_feedback = instance.user_id.username
        title_ad = instance.ad_id.title_ad
        text_feedback = instance.text_feedback
        email_author_ad = instance.ad_id.user_id.email

        send_message_feedback_created.apply_async([author_feedback,
                                                       title_ad,
                                                       text_feedback,
                                                       email_author_ad],)
    else:
        author_ad = instance.ad_id.user_id.username
        title_ad = instance.ad_id.title_ad
        email_author_feedback = instance.user_id.email

        send_message_feedback_accepted.apply_async([author_ad,
                                                       title_ad,
                                                       email_author_feedback],)


@receiver(post_save, sender=News)
def notify_about_news(sender, instance, **kwargs):
    """
    Отправка email в виде рассылки новостей,
    Формируется по сигналу создания новости из панели администратора.
    Рассылка производится всем пользователям из группы Подписчики (Subscribers)

    """


    emails = []
    subscribers = User.objects.filter(groups__name='Subscribers')

    for s in subscribers:
        emails += [s.email]

    send_message_news_created.apply_async([instance.title_news,
                                            instance.text_news,
                                            emails],)
