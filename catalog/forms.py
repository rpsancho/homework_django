from django import forms
from app.common.apps_common import StyleFormMixin, is_acceptable

from catalog.models import Product, Version


class ProductCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        if is_acceptable(cleaned_data):
            return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]

        if is_acceptable(cleaned_data):
            return cleaned_data


class VersionCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
    