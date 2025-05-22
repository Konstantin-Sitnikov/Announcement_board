from django.urls import path


from .views import AdvertisementList, AdDetail, AdCreation, create_feedback, delete_feedback, take_feedback


urlpatterns = [
    path('', AdvertisementList.as_view(), name='ad_list'),
    path('<int:pk>', AdDetail.as_view(), name='ad_detail'),
    path('create', AdCreation.as_view(), name='ad_create'),
    path('<int:pk>/create_feedback', create_feedback, name="create_feedback"),
    path('<int:pk>/delete_feedback', delete_feedback, name="delete_feedback"),
    path('<int:pk>/take_feedback', take_feedback, name="take_feedback"),
]

