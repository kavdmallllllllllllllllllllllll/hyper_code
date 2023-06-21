from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control',}),
            'email' : forms.TextInput(attrs={'class':'form-control',}),
            'password1' : forms.TextInput(attrs={'class':'form-label',}),
            'password2' : forms.TextInput(attrs={'class':'form-label',}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
