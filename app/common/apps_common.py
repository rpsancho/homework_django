from django import forms


class StyleFormMixin():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
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
