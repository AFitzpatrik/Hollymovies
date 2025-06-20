from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.db.transaction import atomic
from django.forms import DateField, NumberInput, CharField, Textarea
from django.views.generic import FormView

from accounts.models import Profile


class MyAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Uživatelské jméno'
        self.fields['password'].label = 'Heslo'


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = 'Staré heslo'
        self.fields['new_password1'].label = 'Nové heslo'
        self.fields['new_password2'].label = 'Potvrzení nového hesla'


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #fields = '__all__'
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

        labels = {
            'username': 'Uživatelské jméno',
            'first_name': 'Jméno',
            'last_name': 'Příjmení',
            'email': 'E-mail',
            'password1': 'Heslo',
            'password2': 'Heslo znovu'
        }

    date_of_birth = DateField(
        widget=NumberInput(attrs={'type': 'date'}),
        label='Datum narození',
        required=False
    )

    biography = CharField(
        widget=Textarea,
        label='Biografie',
        required=False
    )

    phone = CharField(
        label='Telefon',
        required=False
    )


    #ZDE DODĚLAT CLEAN METODY

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)  # vytvoříme uživatele (User)

        # Ještě potřebujeme vytvořit Profile
        date_of_birth = self.cleaned_data.get('date_of_birth')
        biography = self.cleaned_data.get('biography')
        phone = self.cleaned_data.get('phone')
        profile = Profile(
            user=user,
            date_of_birth=date_of_birth,
            biography=biography,
            phone=phone
        )
        if commit:
            profile.save()
        return user