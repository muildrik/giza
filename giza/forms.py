from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tinymce.widgets import TinyMCE

from .models import CustomUser, Collection

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('full_name', 'username', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('full_name', 'username', 'email',)

class CollectionForm(forms.ModelForm):
    title = forms.CharField(required=False, label="Name your new collection")
    class Meta:
        model = Collection
        fields = ('title', )
