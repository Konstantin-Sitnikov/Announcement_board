from django import forms
from .models import Advertisement



class CreationAd(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ["category", "title_ad", "text_ad"]

        def __init__(self, *args, **kwargs):
            """
            Обновление стилей формы под Bootstrap
            """
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})


            self.fields['text_ad'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
            self.fields['text_ad'].required = False



