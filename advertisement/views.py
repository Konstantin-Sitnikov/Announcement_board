from django.views.generic import ListView, DetailView, CreateView
from .models import Advertisement, Feedback
from .forms import CreationAd
from .filters import FeedbackFilter

class AdvertisementList(ListView):
    model = Advertisement
    ordering = 'date_time'
    template_name = 'advertisement/ad_list.html'
    context_object_name = 'ad_list'
    paginate_by = 10


class AdDetail(DetailView):
    model = Advertisement
    template_name = 'advertisement/ad_detail.html'
    context_object_name = 'ad_detail'


class AdCreation(CreateView):
    form_class = CreationAd
    model = Advertisement
    template_name = 'advertisement/ad_creation.html'

    def form_valid(self, form):
        ad = form.save(commit=False)
        user = self.request.user
        ad.user_id = user
        return super().form_valid(form)





class PersonalAccount(ListView):
    ordering = 'date_time'
    template_name = 'advertisement/personal_list.html'
    context_object_name = 'personal_list'

    def get_queryset(self):
        queryset_fedback = Feedback.objects.filter(ad_id__user_id=self.request.user)
        queryset_ad = Advertisement.objects.filter(user_id=self.request.user)
        self.filterset = FeedbackFilter(self.request.GET, queryset_ad=queryset_ad, queryset=queryset_fedback)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filterset'] = self.filterset
        return context