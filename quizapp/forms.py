from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class RegisterUserForm(UserCreationForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # password1 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    # password2 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    # first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('civil_status', 'occupation', 'place_of_residence', 'cellphone', 'level_of_school',)
        widgets = {
            'civil_status': forms.Select(choices=Profile.CIVIL_STATUS_CHOICES),
            'level_of_school': forms.Select(choices=Profile.SCHOOL_LEVEL_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})