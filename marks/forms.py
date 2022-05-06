from django import forms
from django.contrib.auth.models import User



class MarkForm(forms.Form):
    id = forms.IntegerField(label='Id', required=False, widget=forms.HiddenInput)
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, widget=forms.HiddenInput)
    title = forms.CharField(label='Title', max_length=100, required=True
                           ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Image', max_length=100, required=True,
                             widget=forms.FileInput(attrs={'class': 'form-control'}),)
    desctiption = forms.CharField(label='Description', max_length=500, required=True
                                  , widget=forms.Textarea(attrs={'class': 'form-control','rows':'3'}))
    gravity = forms.IntegerField(label='Gravity', required=True
                                 , widget=forms.NumberInput(attrs={'class': 'form-range', 'type': 'range'}))
    created_at = forms.DateField(label='Created_at', required=False)

# class Mark_x_yForm(forms.Form):
#     probleme = forms.ModelChoiceField(queryset=Mark.objects.all(),required=False,widget=forms.HiddenInput)
#     num = forms.IntegerField(null=False, default=1)
#     x = forms.FloatField(null=False)
#     y = forms.FloatField(null=False)
