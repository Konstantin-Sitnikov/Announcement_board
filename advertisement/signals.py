from django.dispatch import receiver
from django.db.models.signals import post_save
from advertisement.models import Feedback
from .tasks import send_message_feedback_created, send_message_feedback_accepted


@receiver(post_save, sender=Feedback)
def notify_about_new_feedback(sender, instance, **kwargs):
    if not instance.feedback_received:
        author_feedback = instance.user_id.username
        title_ad = instance.ad_id.title_ad
        text_feedback = instance.text_feedback
        email_author_ad = instance.ad_id.user_id.email
        print(author_feedback)
        send_message_feedback_created.apply_async([author_feedback,
                                                       title_ad,
                                                       text_feedback,
                                                       email_author_ad],)
    else:
        author_ad = instance.ad_id.user_id.username
        title_ad = instance.ad_id.title_ad
        email_author_feedback = instance.user_id.email
        print(author_ad)
        send_message_feedback_accepted.apply_async([author_ad,
                                                       title_ad,
                                                       email_author_feedback],)


