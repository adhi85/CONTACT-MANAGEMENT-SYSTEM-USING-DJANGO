from django import forms
from .models import ContactDetails
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class ContactForm(forms.ModelForm):
  class Meta:
    model = ContactDetails
    fields = ['photo','fname','lname','gender','age','address','phone','religion','nation']

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		help_texts = {
            'username': None,
            'email': None,
			'password1' : None,
			
        }
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['password1'].help_text='<br> <b>Password should be 8 characters long.</b>'
		self.fields['password2'].help_text=''

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user