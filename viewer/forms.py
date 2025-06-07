from django.forms import Form, CharField


class GenreForm(Form):
    name = CharField(max_length=32, required=True)