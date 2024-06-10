from django import forms
from django.contrib.auth import get_user_model
class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', 
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин',)
    password = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    confirm_password = forms.CharField(label='Повторите пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', 
                               widget=forms.EmailInput(attrs={'class': 'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'confirm_password', 'email', 'first_name', 'last_name']
        labels = {'password': 'Пароль', 
                'confirm_password': 'Повторите пароль',
                'first_name': 'Имя',
                'last_name': 'Фамилия',
                'email': 'Email',
                'username': 'Логин'
                }
    
    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует!')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует!')
        return username
