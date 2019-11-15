from django import forms

class Contacto(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class' : 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class' : 'form-control-is-invalid'}))
    mensaje = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'placeholder': 'Mensaje', 'class' : 'form-control'}))
