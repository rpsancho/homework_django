from django import forms

from blog.models import Blog


class StyleFormMixin():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


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


class BlogCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('slug', 'views_count')

    def clean_title(self):
        cleaned_data = self.cleaned_data["title"]

        if is_acceptable(cleaned_data):
            return cleaned_data

    def clean_content(self):
        cleaned_data = self.cleaned_data["content"]

        if is_acceptable(cleaned_data):
            return cleaned_data
