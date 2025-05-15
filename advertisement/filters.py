import django_filters
from django_filters import FilterSet
from .models import Advertisement, Feedback



def get_user(request):
    return Advertisement.objects.filter(user_id=request.user)



class FeedbackFilter(FilterSet):
    ad_id = django_filters.ModelChoiceFilter(queryset=Advertisement.objects.all(), label="Объявление")

    class Meta:
        model = Feedback
        fields = [  ]


