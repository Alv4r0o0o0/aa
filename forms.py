from django import forms
from . models import Articulos, Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'nombre',
            'apellido',
            'email',
            'tfno',
            'clave',
            'confirmar_clave',
            'direccion'
]
        
class Usuario2Form(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'nombre',
            'apellido',
            'email',
            'tfno',
            'direccion'
]        

        
class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields =[
            'nombre',
            'descripcion',
            'precio',
            'stock',
            'foto',
            'marca',
            'precio_oferta',
            'descuento',
           
        ]
    def clean(self):
        cleaned_data = super().clean()
        precio = cleaned_data.get('precio')
        descuento = cleaned_data.get('descuento')

        if precio and descuento:
            cleaned_data['precio_oferta'] = precio - (precio * (descuento / 100))

        return cleaned_data    


from django import forms





from django import forms
from .models import Articulos, Imagen
from django.forms.models import inlineformset_factory

from django import forms
from .models import Articulos, Imagen
from django.forms.models import inlineformset_factory

class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'foto', 'marca', 'precio_oferta', 'descuento']

ImagenFormSet = inlineformset_factory(Articulos, Imagen, fields=['imagen'], extra=1, can_delete=True)

        
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))   

from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['rut_empresa', 'nombre_empresa', 'representante_legal', 'contacto_empresa', 'direccion_proveedor', 'email_proveedor']
