from django.views.generic import ListView, DetailView
from .models import Advertisement


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