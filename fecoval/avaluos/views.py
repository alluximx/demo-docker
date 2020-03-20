from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class AvaluoList(LoginRequiredMixin, View):
    def get(self, request):
        template = 'avaluos/list.html'
        context = {
            'avaluos_page': 'active'
        }
        return render(request, template, context=context)


class AvaluoCreate(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'altas_page': 'active'
        }
        template = 'avaluos/create.html'
        return render(request, template, context=context)
