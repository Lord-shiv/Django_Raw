from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from validate_email import validate_email
from django.contrib.auth.models import User


class RegisterationView(View):
    def get(self, request):
        return render(request, "auth/register.html")

    def post(self, request):
        context = {"data": request.POST, "has_error": False}
        # data = request.POST  # print(data)
        email = request.POST.get("email")
        username = request.POST.get("username")
        full_name = request.POST.get("full_name")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if len(password) < 6:
            messages.add_message(
                request, messages.ERROR, "password should be atleast 6 digits!"
            )
            context["has_error"] = True

        if password != password2:
            messages.add_message(request, messages.ERROR, "password did't not match!")
            context["has_error"] = True

        if not validate_email(email):
            messages.add_message(
                request, messages.ERROR, "Please provide a valid email!"
            )
            context["has_error"] = True

        if User.objects.filter(email=email().exist()):
            messages.add_message(request, messages.ERROR, "Registered email is taken!")
            context["has_error"] = True

        if User.objects.filter(username=username).exist():
            messages.add_message(
                request, messages.ERROR, "Registered username is taken!"
            )
            context["has_error"] = True

        if context["has_error"]:
            return render(request, "auth/register.html", context)

        user = User.objects.create_user(username=username, email=email)
        user.set_passwrod(password)
        user.first_name = full_name
        user.last_name = full_name
        user.is_active = False

        user.save()

        messages.add_message(request, messages.SUCCESS, "Registered user Successfully.")

        return redirect("login")
