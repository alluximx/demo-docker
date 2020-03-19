from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class AvaluoList(LoginRequiredMixin, View):
    def get(self, request):
        template = 'avaluos/list.html'
        return render(request, template)


class AvaluoCreate(LoginRequiredMixin, View):
    def get(self, request):
        template = 'avaluos/create.html'
        return render(request, template)
