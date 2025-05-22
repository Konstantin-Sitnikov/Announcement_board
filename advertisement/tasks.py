from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from Announcement_board.settings import SITE_URL, DEFAULT_FROM_EMAIL

from celery import shared_task


@shared_task()
def send_message_feedback_created(user_name, title_ad, text_feedback, email):
    """Отправка сообщения о новом отклике к объявлению"""
    html_content = render_to_string(
        'emails/send_message_feedback_created.html',
        {
            'user_name': user_name,
            'title': title_ad,
            'text': text_feedback
            #'link': f'{SITE_URL}/{pk}'

        }
    )
    msg = EmailMultiAlternatives(
        subject='Новый отклик',
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=[email]
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()




@shared_task()
def send_message_feedback_accepted(user_name, title_ad, email):
    """Отправка сообщения отклик принят"""

    html_content = render_to_string(
        'emails/send_message_feedback_accepted.html',
        {
            'user_name': user_name,
            'title': title_ad,

            #'link': f'{SITE_URL}/{pk}'

        }
    )
    msg = EmailMultiAlternatives(
        subject='Ваш отклик принят',
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=[email]
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task()
def send_message_news_created(title_news, text_news,  email):
    """Рассылка новостей пользователям которые подписались на рассылку"""
    html_content = render_to_string(
        'emails/send_message_news.html',
        {
            'title_news': title_news,
            'text_news': text_news,


            # 'link': f'{SITE_URL}/{pk}'

        }
    )
    msg = EmailMultiAlternatives(
        subject='"Важная" новость',
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=email
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
