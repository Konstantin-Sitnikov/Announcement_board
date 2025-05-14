from django.views.generic import ListView, DetailView, CreateView
from .models import Advertisement
from .forms import CreationAd


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

