from django import forms


class StyleFormMixin():

    BOOL_FIELDS = ['is_published', 'is_current_version',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in self.BOOL_FIELDS:
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
