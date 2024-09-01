from django import forms
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
        fields = ('username', 'email')
        
    