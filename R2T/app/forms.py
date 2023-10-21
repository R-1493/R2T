
from django import forms
from django.contrib.auth.forms import UserCreationForm #for ising the sign up form that is ready
from django.db import transaction
from .models import Customer, User, Translatorr
from django.core.validators import MaxValueValidator, MinValueValidator




#====================================================================================================
#Starn sign Up forms
#====================================================================================================
#************Start customer sign up form that hasdeffrent requirement********************************
class CustomerSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)#-----
    age=forms.CharField(required=True)#-----
    F1_Language = [
        ('AR', 'Arabic'),
        ('EN', 'English'),
        ('FR', 'France'),
        ('es', 'Spanish'),
        ('so', 'Somalia'),
        ('ru', 'Russian'),
        ('sq', 'Albanian'),
        ('th', 'Thai'),
        ('tr', 'Turkish'),
        ('ur', 'Urdu'),
        ('so', 'Chinese'),
        ('zh', 'Russian'),]
        
    First_Language=forms.ChoiceField(choices=F1_Language)#-----testing
    email=forms.EmailField(required=True)#-----
    phoneNumber = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label="Phone number")
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')#-----
        user.is_customer = True
        user.save()
        student = Customer.objects.create(user=user)
        student.name=self.cleaned_data.get('name')#-----
        student.age=self.cleaned_data.get('age') #-----  
        student.First_Language=self.cleaned_data.get('First_Language')#-----
        student.phoneNumber=self.cleaned_data.get('phoneNumber')#-----
        student.save()
        return user
#********************translator sign up form that hasdeffrent requirement *******************
class TranslatorSignUpForm(UserCreationForm):
    name=forms.CharField(required=True, label="Username: ")#-----
    age=forms.CharField(required=True)#-----
    F1_Language = [
        ('AR', 'Arabic'),
        ('EN', 'English'),
        ('FR', 'France'),
        ('es', 'Spanish'),
        ('so', 'Somalia'),
        ('ru', 'Russian'),
        ('sq', 'Albanian'),
        ('th', 'Thai'),
        ('tr', 'Turkish'),
        ('ur', 'Urdu'),
        ('so', 'Chinese'),
        ('zh', 'Russian'),]

    F2_Language = [
        ('AR', 'Arabic'),
        ('EN', 'English'),
        ('FR', 'France'),
        ('es', 'Spanish'),
        ('so', 'Somalia'),
        ('ru', 'Russian'),
        ('sq', 'Albanian'),
        ('th', 'Thai'),
        ('tr', 'Turkish'),
        ('ur', 'Urdu'),
        ('so', 'Chinese'),
        ('zh', 'Russian'),]
    First_Language=forms.ChoiceField(choices=F1_Language)#-----testing
    Cert = [
            ('Bachelor degree', 'Bachelor degree'),
            ('Diploma degree', 'Diploma degree'),
            ('Courses', 'Courses'),
            ('Experience', 'Experience'),
        ]
    Second_Language=forms.ChoiceField(choices=F2_Language)#-----testing
    Certification=forms.ChoiceField(choices=Cert)#-----
    email=forms.EmailField(required=True)#-----
    phoneNumber = forms.RegexField(regex=r'^\+?1?\d{9,15}$',  label="Phone number")
    price = forms.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')#-----
        user.is_translator = True
        user.save()
        translator = Translatorr.objects.create(user=user)
        translator.name=self.cleaned_data.get('name')#-----
        translator.age=self.cleaned_data.get('age') #-----  
        translator.First_Language=self.cleaned_data.get('First_Language')#-----
        translator.Second_Language=self.cleaned_data.get('Second_Language')#-----
        translator.Certification=self.cleaned_data.get('Certification')#-----
        translator.phoneNumber=self.cleaned_data.get('phoneNumber')#-----
        translator.price=self.cleaned_data.get('price')#-----
        translator.save()
        return user
#====================================================================================================
#End sign Up forms
#====================================================================================================


#====================================================================================================
#Start log in forms
#====================================================================================================
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
#====================================================================================================
#End log in forms
#====================================================================================================
