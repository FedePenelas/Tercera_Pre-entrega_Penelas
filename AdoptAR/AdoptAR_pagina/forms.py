from django import forms

class FormularioPersona(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30)
    apellido = forms.CharField(label='Apellido', max_length=20)
    email = forms.EmailField(label='E-mail')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)

class FormularioDonante(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30)
    apellido = forms.CharField(label='Apellido', max_length=20)
    email = forms.EmailField(label='E-mail')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)

class FormularioTransito(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30)
    apellido = forms.CharField(label='Apellido', max_length=20)
    email = forms.EmailField(label='E-mail')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)

class FormularioDarEnAdopcion(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30)
    apellido = forms.CharField(label='Apellido', max_length=20)
    email = forms.EmailField(label='E-mail')
    animal = forms.CharField(label="Animal")
    edadanimal = forms.IntegerField()
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)
