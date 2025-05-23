from django.shortcuts import redirect
from django.views.generic import ListView

from django.contrib.auth.models import Group
from advertisement.filters import FeedbackFilter
from advertisement.models import Feedback, Advertisement


class PersonalAccount(ListView):
    ordering = 'date_time'
    template_name = 'personal_account/personal_account.html'
    context_object_name = 'personal_list'
    paginate_by = 10

    def get_queryset(self):
        queryset_fedback = Feedback.objects.filter(ad_id__user_id=self.request.user)
        queryset_ad = Advertisement.objects.filter(user_id=self.request.user)
        self.filterset = FeedbackFilter(self.request.GET, queryset_ad=queryset_ad, queryset=queryset_fedback)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['current_user'] = self.request.user
        return context


def subscribe_to_news(request):
    user = request.user
    subscribe_group = Group.objects.get(name='Subscribers')
    if not request.user.groups.filter(name='Subscribers').exists():
        subscribe_group.user_set.add(user)

    return redirect('/personal_account/')

def unsubscribe_to_news(request):
    user = request.user
    subscribe_group = Group.objects.get(name='Subscribers')
    if request.user.groups.filter(name='Subscribers').exists():
        subscribe_group.user_set.remove(user)

    return redirect('/personal_account/')
