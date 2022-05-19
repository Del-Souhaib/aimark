from django import forms
from django.contrib.auth.models import User
from django.http import request


class UserForm(forms.Form):
    id = forms.IntegerField(label='Id', required=False, widget=forms.HiddenInput)
    username = forms.CharField( required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', max_length=100, required=True
                           ,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=100, required=False,
                             widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
    verifypassword = forms.CharField(label='Verify password', max_length=100, required=False,
                             widget=forms.PasswordInput(attrs={'class': 'form-control'}),)

    date_joined = forms.DateField(label='date_joined', required=False)
    editprofile=forms.CharField(initial=False)
    # def validation(self):
    #     if self.editprofile == True and self.password != self.verifypassword:
    #         self.add_error('verifypassword','password dosent match')





