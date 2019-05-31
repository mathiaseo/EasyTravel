from django import forms
from models import *

class User_BookForm(forms.ModelForm):
    user_password = forms(CharField(widget=forms.PasswordInput))

    class Meta:
        model = User_Book
        fields = ('user_idBook','user_mail_add','user_city','user_state','user_last_name','user_first_name','user_password')