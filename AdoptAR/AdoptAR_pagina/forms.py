from django import forms
from .models import *

class FormularioPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class FormularioDonante(forms.ModelForm):
    class Meta:
        model = Donante
        fields = '__all__'

class FormularioTransito(forms.ModelForm):
    class Meta:
        model = Transito
        fields = '__all__'

class FormularioDarEnAdopcion(forms.ModelForm):
    class Meta:
        model = DarEnAdopcion
        fields = '__all__'


from .models import Persona, DarEnAdopcion, Transito, Donante

class FormularioGenerico(forms.ModelForm):
    class Meta:
        model = None
        fields = '__all__'

class BusquedaForm(forms.Form):
    criterio = forms.CharField(label='Criterio de búsqueda', max_length=100)