from django import forms

class Contacto(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control is-invalid'}))
    mensaje = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'placeholder': 'Mensaje', 'class': 'form-control'}))

class Registro(forms.Form):
    usuario = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class':'form-control'}))
    contraseña = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs ={ 'placeholder': 'Contraseña', 'class':'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico', 'class':'form-control'}))
