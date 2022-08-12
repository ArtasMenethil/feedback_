from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Введите логин', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Введите пароль', required=True,
                               help_text='Пароль не должен быть простым',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Введите логин', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(label='Загрузить фото', required=False,
                           widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['img']
