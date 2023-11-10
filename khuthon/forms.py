from django import forms
from khuthon.models import UserInfo

class basicForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['userID', 'gender', 'age']