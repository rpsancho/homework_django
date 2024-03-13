from django import forms

from catalog.models import Product


def is_acceptable(data):
    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    for word in forbidden_words:
        if word in data:
            raise forms.ValidationError("Текст содержит запрещённые слова")

    return True


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        if is_acceptable(cleaned_data):
            return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]

        if is_acceptable(cleaned_data):
            return cleaned_data
