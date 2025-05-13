from django.views.generic import ListView
from .models import Advertisement


class AdvertisementList(ListView):
    model = Advertisement
    ordering = 'date_time'
    template_name = 'advertisement/ad_list.html'
    context_object_name = 'ad_list'
    paginate_by = 1