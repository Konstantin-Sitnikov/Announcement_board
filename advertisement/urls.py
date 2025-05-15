from django.urls import path


from .views import AdvertisementList, AdDetail, AdCreation, PersonalAccount

urlpatterns = [
    path('', AdvertisementList.as_view(), name='ad_list'),
    path('<int:pk>', AdDetail.as_view(), name='ad_detail'),
    path('create', AdCreation.as_view(), name='ad_create'),
    path('personal_account', PersonalAccount.as_view(), name='personal_account')

]

