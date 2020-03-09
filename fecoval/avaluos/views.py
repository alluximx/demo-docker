from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . forms import AltaAvaluoForm1, MancomunadoForm, DatosClienteForm, ClienteForm


@login_required
def avaluos_list(request):
    template = 'avaluos/list.html'
    return render(request, template)


@login_required
def avaluos_create(request):

    cliente_form = ClienteForm()
    avaluo_form = AltaAvaluoForm1(prefix="avaluo1")
    mancomunado_form = MancomunadoForm(prefix="mancomunado")
    datoscliente_form = DatosClienteForm(prefix="datos-cliente")
    # datoscliente_formset = DatosClienteFormset()
    template = 'avaluos/create.html'
    context = {
        'avaluo_form': avaluo_form,
        # 'datoscliente_formset': datoscliente_formset,
        'mancomunado_form': mancomunado_form,
        'cliente_form': cliente_form,
        'datoscliente_form': datoscliente_form,
    }
    return render(request, template, context)
