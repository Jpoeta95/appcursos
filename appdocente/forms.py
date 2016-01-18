from django import forms
from .models import docente

class docenteForm(forms.ModelForm):
    class Meta:
        model = docente
        fields = '__all__'
        no = {'class':'form-control', 'placeholder':'ingresar nombre'}
        tp = {'class':'form-control'}
        

        labels = {
            'nombre' : ('Ingresar nombre'),
            'ape_pat' : ('Ingresar Apellido Paterno'),
            'ape_mat' : ('Ingresar Apellido Materno'),
            'docente_curso': ('seleccione cursos')
        }
        widgets = {
            'nombre' : forms.TextInput(attrs=no),
            'ape_pat'        : forms.TextInput(attrs=tp),
            'ape_mat'         : forms.TextInput(attrs=tp),
            'dni'            : forms.NumberInput(attrs=tp),
            'docente_curso'       :forms.SelectMultiple(attrs=tp)
        }
        help_texts = {
            'dni': ('** No escribir mas de 8 digitos.<br>'),
        }
        error_messages = {
            'dni': {
                'max_length': ("Dni Muy largo."),
            },
        }
