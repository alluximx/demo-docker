from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class AvaluosList(LoginRequiredMixin, View):

    def get(self, request):
        template = 'pages/home.html'
        return render(request, template)
