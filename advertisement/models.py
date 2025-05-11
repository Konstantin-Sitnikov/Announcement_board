from django.db import models
from django.contrib.auth.models import User

class Category(models.Model): # модель категории
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name



class Advertisement(models.Model): # модель объявления
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title_ad = models.CharField(max_length=128)
    text_ad = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_ad



class Feedback(models.Model): # модель отклика
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text_feedback = models.CharField(max_length = 255)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_feedback



class News(models.Model): # модель новостей
    title_news = models.CharField(max_length=128)
    text_news = models.TextField()
