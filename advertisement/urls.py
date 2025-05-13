from django.urls import path

from .views import AdvertisementList

urlpatterns = [
   path('', AdvertisementList.as_view()),
]

