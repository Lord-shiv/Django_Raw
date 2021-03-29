from django.shortcuts import render
from django.views.generic import View


class RegisterationView(View):
    def get(self, request):
        return render(request, "auth/register.html")
