from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from . models import DatosCliente, Cliente, Avaluo, Mancomunado, Estado, Municipio, ADR


class ClienteForm(forms.ModelForm):

    cliente = forms.ModelChoiceField(
        required=True, queryset=Cliente.objects.all()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('cliente', css_class='form-group col-md-4 mb-0'),
                css_class='form_row'
            ),
        )

    class Meta:
        model = Cliente
        fields = ('cliente',)


class DatosClienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('persona', css_class='form-group col-md-4 mb-0'),
                css_class='form_row'
            ),
            Row(
                Column('nombre', css_class='form-group col-md-4 mb-0'),
                Column('apellido_paterno', css_class='form-group col-md-4 mb-0'),
                Column('apellido_materno', css_class='form-group col-md-4 mb-0'),
                css_class='form_row'
            ),
            Row(
                Column('rfc', css_class='form-group col-md-3 mb-0'),
                Column('curp', css_class='form-group col-md-3 mb-0'),
                Column('nss', css_class='form-group col-md-3 mb-0'),
                Column('telefono', css_class='form-group col-md-3 mb-0'),
            )
        )

    class Meta:
        model = DatosCliente
        fields = ('persona', 'nombre', 'apellido_paterno', 'apellido_materno', 'rfc', 'curp', 'nss', 'telefono')


class MancomunadoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-3 mb-0'),
                Column('rfc', css_class='form-group col-md-3 mb-0'),
                Column('telefono', css_class='form-group col-md-3 mb-0'),
                Column('celular', css_class='form-group col-md-3 mb-0'),
                css_class='form_row'
            ),
        )

    class Meta:
        model = Mancomunado
        fields = ('nombre', 'rfc', 'telefono', 'celular')


class AltaAvaluoForm1(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('folio', css_class='form-group col-md-4 mb-0'),
                Column('fecha_asignacion', css_class='form-group col-md-4 mb-0'),
                Column('fecha_compromiso', css_class='form-group col-md-4 mb-0'),
                Column('fecha_solicitud_correo', css_class='form-group col-md-4 mb-0'),
                Column('credito_fiscal', css_class='form-group col-md-4 mb-0'),
                css_class='form_row'
            ),
        )

    class Meta:
        model = Avaluo
        fields = ('folio', 'fecha_asignacion', 'fecha_compromiso', 'fecha_solicitud_correo', 'credito_fiscal', 'codigo_postal', 'calle', 'no_ext', 'no_int', 'colonia', 'lote', 'manzana')


class AltaAvaluoForm2(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('codigo_postal', css_class='form-group col-md-3 mb-0'),
                Column('calle', css_class='form-group col-md-3 mb-0'),
                Column('no_ext', css_class='form-group col-md-3 mb-0'),
                Column('no_int', css_class='form-group col-md-3 mb-0'),
                css_class='form_row'
            ),
            Row(
                Column('colonia', css_class='form-group col-md-3 mb-0'),
                Column('lote', css_class='form-group col-md-3 mb-0'),
                Column('manzana', css_class='form-group col-md-3 mb-0'),
                css_class='form_row'
            ),
        )

    class Meta:
        model = Avaluo
        fields = ('codigo_postal', 'calle', 'no_ext', 'no_int', 'colonia', 'lote', 'manzana')
