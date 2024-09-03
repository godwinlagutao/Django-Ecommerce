from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User # for creating users
from django.contrib.auth.forms import UserCreationForm, UserChangeForm#for creating user forms

class UserUpdateForm(UserChangeForm):
    password = forms.CharField(
		widget=forms.PasswordInput,
		required= False,
		help_text= 'Leave blank if you do not want to change pasword.'
	) # password field is not required
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
    
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})