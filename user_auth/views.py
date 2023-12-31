import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from user_auth.forms import UserRegisterForm
from user_auth.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user_auth/register.html'
    success_url = reverse_lazy('user_auth:verification')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            subject = 'Одноразовый код'
            message = f"""Данный код является одноразовым для подтверждения регистрации
            {new_user.verification_code}"""
            send_mail(subject, message, settings.EMAIL_HOST_USER, [new_user.email])

        return super().form_valid(form)


class VerificationTemplateView(TemplateView):
    template_name = 'user_auth/verification.html'

    def post(self, request):
        verification_code = request.POST.get('verification_code')
        user_code = User.objects.filter(verification_code=verification_code).first()
        if user_code is not None and user_code.verification_code == verification_code:
            user_code.is_active = True
            user_code.save()
            return redirect('user_auth:login')
        else:
            return redirect('user_auth:error_user')


class RecoveryTemplateView(TemplateView):
    template_name = 'user_auth/recovery_pass.html'

    def post(self, request):
        email = request.POST.get('email')
        email_user = User.objects.filter(email=email).first()
        if email_user:
            #Генерирую новый пароль
            list_password = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            list_code = random.sample(list_password, 10)
            result = ''.join(list_code)
            #Переопределяю для пользователя новый пароль и отправляю письмо
            email_user.set_password(result)
            email_user.save()
            subject = 'Одноразовый код'
            message = f"""Данный код является вашим новым паролем в системе
                        {result}"""
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email_user.email])
        return redirect('user_auth:login')


class ErrorVerificationTemplateView(TemplateView):
    template_name = 'user_auth/error_user.html'
    success_url = reverse_lazy('user_auth:verification')


