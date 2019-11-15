from django import forms
from django.contrib.auth import get_user_model
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Cliente

class defaultForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text =' Requerido, 254 caracteres como máximo y debe ser valido')
    class Meta:
        model = User
        fields = ['username','password1','password2','email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control mb-2 ','placeholder':'Usuario'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control  mb-2','placeholder':'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control  mb-2','placeholder':'Repita Contraseña'}),
            'email': forms.EmailInput(attrs={'class':'form-control  mb-2','placeholder':'Correo'}),
        }
        labels = {
            'username':'',
            'password1': '',
            'password2': '',
            'email': '',
        }
    #metodo para que no se ingresen email que ya se ingresaron previamente
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("El email ya esta registrado, prueba con otro")
        return email
    
class cliForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['correo','nombre','apellido','rut','telefono']
        widgets = {
            'correo': forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Repita Email'}),
            'nombre': forms.TextInput(attrs={'class':'form-control  mb-2 required','placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'form-control  mb-2','placeholder':'Apellido'}),
            'rut': forms.TextInput(attrs={'class':'form-control  mb-2','placeholder':'RUT'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control  mb-2','placeholder':'Teléfono'}),
        }
        labels = {
            'correo': '',
            'nombre': '',
            'apellido': '',
            'rut': '',
            'telefono': '',
        }


class ClienteForm(MultiModelForm):

    form_classes = {
        'user': defaultForm,
        'cliente': cliForm, 
    }