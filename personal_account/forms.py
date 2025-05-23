from allauth.account.forms import forms, SignupForm
from django.contrib.auth.models import Group


class BasicSignupForm(SignupForm):
    last_name = forms.CharField(max_length=20)
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='Standard')
        basic_group.user_set.add(user)
        return user