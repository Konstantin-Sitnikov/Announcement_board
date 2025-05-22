from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import Advertisement, Feedback
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

    def get_context_data(self, **kwargs):
        ad = self.get_object()
        if ad.user_id == self.request.user:
            author_ad = True
        else:
            author_ad = False
        context = super().get_context_data(**kwargs)
        context['feedbacks'] = Feedback.objects.filter(ad_id=ad.pk)
        context['author_ad'] = author_ad
        return context


class AdCreation(CreateView):
    form_class = CreationAd
    model = Advertisement
    template_name = 'advertisement/ad_creation.html'

    def form_valid(self, form):
        ad = form.save(commit=False)
        user = self.request.user
        ad.user_id = user
        return super().form_valid(form)


def create_feedback(request, pk):
    if request.method == "POST":
        feedback = Feedback(ad_id=Advertisement.objects.get(pk=pk), user_id=request.user, text_feedback=request.POST.get("text"))
        feedback.save()
        print(feedback.ad_id.user_id.email)
        return redirect("ad_detail", pk)


def delete_feedback(request, pk):
    if request.method == "POST":
        feedback = Feedback.objects.get(pk=pk)
        feedback.delete()
        return redirect("personal_account")


def take_feedback(request, pk):
    if request.method == "POST":
        feedback = Feedback.objects.get(pk=pk)
        feedback.feedback_received = True
        feedback.save()
        return redirect("personal_account")


