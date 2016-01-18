from django import forms
from .models import alumno

class alumnoForm(forms.ModelForm):
    class Meta:
        model = alumno
        fields = '__all__'
        no = {'class':'form-control', 'placeholder':'ingresar nombre'}
        tp = {'class':'form-control'}
        

        labels = {
            'descripcionalumno' : ('Ingresar nombre'),
            'dni' : ('Ingresar Apellido Paterno'),
            'fechanac' : ('Ingresar fecha de nacimiento'),
            'alumno_docente': ('seleccione docente'),
            'alumno_curso': ('seleccione cursos')
        }
        widgets = {
            'descripcionalumno': forms.TextInput(attrs=no),
            'fechanac'         : forms.DateInput(attrs=tp),
            'alumno_docente'   : forms.SelectMultiple(attrs=tp),
            'dni'              : forms.TextInput(attrs=tp),
            'alumno_curso'     : forms.SelectMultiple(attrs=tp)
        }
        help_texts = {
            'dni': ('** No escribir mas de 8 digitos.<br>'),
        }
        error_messages = {
            'dni': {
                'max_length': ("Dni Muy largo."),
            },
        }
