from django import forms
from .models import RegisterModel

class RegisterForm(forms.ModelForm):
    Re_enter_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = RegisterModel
        fields = ['first_name','last_name','username','email','Phone_no','password','Re_enter_password']
    def clean(self):
        password = self.cleaned_data['password']
        re_enter_pass = self.cleaned_data['Re_enter_password']

        if(password != re_enter_pass):
            raise forms.ValidationError("Password is not Match")    