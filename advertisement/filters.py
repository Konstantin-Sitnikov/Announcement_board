import django_filters
from django_filters import FilterSet
from .models import Advertisement, Feedback



class FeedbackFilter(FilterSet):
    ad_id = django_filters.ModelChoiceFilter(queryset=Advertisement.objects.all(), label="Объявление")


    def __init__(self, *args, **kwargs):
        self.queryset_ad = kwargs.pop('queryset_ad', None)
        super(FeedbackFilter, self).__init__(*args, **kwargs)
        self.filters['ad_id'].queryset = self.queryset_ad

    class Meta:
        model = Feedback
        fields = [ 'ad_id' ]




