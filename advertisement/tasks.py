from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from Announcement_board.settings import SITE_URL, DEFAULT_FROM_EMAIL

from celery import shared_task


@shared_task()
def send_message_feedback_created(user, title_ad, text_feedback, email):
    """Отправка сообщения о новом отклике к объявлению"""
    html_content = render_to_string(
        'post_created_email.html',
        {
            'user': user,
            'title': title_ad,
            'text': text_feedback
            #'link': f'{SITE_URL}/{pk}'

        }
    )
    msg = EmailMultiAlternatives(
        subject='title',
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=email
    )

    pass




@shared_task()
def send_message_feedback_accepted():
    """Отправка сообщения отклик принят"""
    pass
