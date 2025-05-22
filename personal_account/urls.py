from django.urls import path


from personal_account.views import PersonalAccount, subscribe_to_news, unsubscribe_to_news


urlpatterns = [
    path('', PersonalAccount.as_view(), name='personal_account'),
    path('subscribe', subscribe_to_news, name='subscribe'),
    path('unsubscribe', unsubscribe_to_news, name='unsubscribe'),

]

