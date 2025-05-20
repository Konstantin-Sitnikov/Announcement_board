from django.dispatch import receiver
from django.db.models.signals import post_save
from advertisement.models import Feedback
from .tasks import send_message_feedback_created


@receiver(post_save, sender=Feedback)
def notify_about_new_feedback(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        author_feedback = instance.user_id
        title_ad = instance.ad_id.title_ad
        text_feedback = instance.text_feedback
        email_author_ad = instance.ad_id.ad_id.user_id.email

        send_message_feedback_created.apply_async({"user": author_feedback ,'email': instance.user_id.email}, )


