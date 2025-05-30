from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    """Модель Категорий"""
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name



class Advertisement(models.Model):
    """Модель Объявлений"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title_ad = models.CharField(max_length=128)
    text_ad = CKEditor5Field()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_ad

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])



class Feedback(models.Model):
    """Модель Отклика"""
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text_feedback = models.CharField(max_length = 255)
    feedback_received = models.BooleanField(default = False)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_feedback



class News(models.Model):
    """
        Модель Категорий
        Отправка новостей возможна только из админ панели
    """
    title_news = models.CharField(max_length=128)
    text_news = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_news
