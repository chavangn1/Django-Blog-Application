from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name','phone_number','password')

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        phone_number = self.cleaned_data.get('phone_number')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        if phone_number and len(phone_number) != 10 and not phone_number.isdigit():
            raise forms.ValidationError("Phone Number is incorrect")
        
        return self.cleaned_data