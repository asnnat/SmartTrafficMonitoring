from django import forms
from django.contrib.auth.models import User
from .models import UserInfo, RoleID


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=10, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        try:
            # set the initial value of phone_number field to user's phone_number value in UserInfo
            user_info = UserInfo.objects.get(user_id=self.instance)
            self.fields['phone_number'].initial = user_info.phone_number
        except UserInfo.DoesNotExist:
            pass

    def save(self, commit=True):
        # save the phone_number value to UserInfo
        user_info, _ = UserInfo.objects.get_or_create(user_id=self.instance)
        user_info.phone_number = self.cleaned_data['phone_number']
        user_info.save()
        return super().save(commit)

class UserCreationForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'role_id': forms.HiddenInput(attrs={'value': 3}),
            'role_id_id': forms.HiddenInput(),
            'role_id__name': forms.TextInput(attrs={'disabled': True}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            UserInfo.objects.create(user_id=user, role_id_id=3, phone_number=self.cleaned_data['phone_number'])
        return user