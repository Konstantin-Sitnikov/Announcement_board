from django.contrib import admin
from .models import Advertisement, Category, Feedback, News

# Register your models here.

admin.site.register(Advertisement)
admin.site.register(Category)
admin.site.register(Feedback)
admin.site.register(News)
