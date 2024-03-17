from django import forms


class StyleFormMixin():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'is_published':
                field.widget.attrs['class'] += ' form-check-input'


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
