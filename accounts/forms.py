from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','full_name','phone_number','password','confirm_password',)


    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        phone_number = cleaned_data.get('phone_number')

        # Password validation
        if password and confirm_password:
            if password != confirm_password:
                self.add_error(
                    'confirm_password',
                    'Passwords do not match.'
                )

        # Phone validation
        if phone_number:
            if len(phone_number) != 10 or not phone_number.isdigit():
                self.add_error(
                    'phone_number',
                    'Phone number must contain exactly 10 digits.'
                )

        return cleaned_data
