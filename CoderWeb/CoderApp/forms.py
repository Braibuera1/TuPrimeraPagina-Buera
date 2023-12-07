from django import forms
from .models import Terror,Comedia,Cienciaficcion


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Terror
        fields = ['titulo','año','director']
        
class ComediaForm(forms.ModelForm):
    class Meta:
        model = Comedia
        fields = ['titulo','año','director']

class CienciaficcionForm(forms.ModelForm):
    class Meta:
        model = Cienciaficcion
        fields = ['titulo','año','director']                