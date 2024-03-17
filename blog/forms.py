from django import forms
from app.common.apps_common import StyleFormMixin, is_acceptable

from blog.models import Blog


class BlogCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('slug', 'creation_date', 'views_count',)

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']

        if is_acceptable(cleaned_data):
            return cleaned_data

    def clean_content(self):
        cleaned_data = self.cleaned_data['content']

        if is_acceptable(cleaned_data):
            return cleaned_data
