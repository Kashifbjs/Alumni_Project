from django import forms
from django.core import validators
from django.utils.html import format_html

class Login_Form(forms.Form):
    User_Name = forms.CharField()
    Password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id' : 'id_Password_1'}),
        label='Password'
    )
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['User_Name'].widget.attrs['class'] = 'form-control'
        self.fields['User_Name'].label = 'UserName '
        self.fields['Password'].widget.attrs['class'] = 'form-control'

class Register_Form(forms.Form):
    User_Name = forms.CharField()
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    Email = forms.EmailField()
    Password = forms.CharField()
    Password2 = forms.CharField()
    USER_CHOICES = [
        ('alumni', 'Alumni'),
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]
    Chk_Role = forms.ChoiceField(choices=USER_CHOICES)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['User_Name'].widget.attrs['class'] = 'form-control'
        self.fields['First_Name'].widget.attrs['class'] = 'form-control'
        self.fields['Last_Name'].widget.attrs['class'] = 'form-control'
        self.fields['Email'].widget.attrs['class'] = 'form-control'
        self.fields['Password'].widget.attrs['class'] = 'form-control'
        self.fields['Password2'].widget.attrs['class'] = 'form-control'
        self.fields['Password2'].label = 'Confirm Password '
        self.fields['Chk_Role'].widget.attrs['class'] = 'form-control'
        self.fields['Chk_Role'].label = 'Select Designation'
    
    def clean(self):
        all_clean_data = super().clean()
        Password = all_clean_data['Password']
        Password2 = all_clean_data['Password2']

        if Password != Password2:
            raise forms.ValidationError('Make Sure Both Password match...!')