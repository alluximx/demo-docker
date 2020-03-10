from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . forms import AltaAvaluoForm1, AltaAvaluoForm2, MancomunadoForm, DatosClienteForm, ClienteForm


@login_required
def avaluos_list(request):
    template = 'avaluos/list.html'
    return render(request, template)


@login_required
def avaluos_create(request):

    cliente_form = ClienteForm(prefix="cliente")
    avaluo1_form = AltaAvaluoForm1(prefix="avaluo1")
    avaluo2_form = AltaAvaluoForm2(prefix="avaluo2")
    mancomunado_form = MancomunadoForm(prefix="mancomunado")
    datoscliente_form = DatosClienteForm(prefix="datos-cliente")
    # datoscliente_formset = DatosClienteFormset()
    template = 'avaluos/create.html'
    context = {
        'avaluo1_form': avaluo1_form,
        'avaluo2_form': avaluo2_form,
        # 'datoscliente_formset': datoscliente_formset,
        'mancomunado_form': mancomunado_form,
        'cliente_form': cliente_form,
        'datoscliente_form': datoscliente_form,
    }
    return render(request, template, context)
