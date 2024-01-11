
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from users.forms import UserAuthenticationForm, UserProfileForm, UserRegisterForm
from users.models import User
from django.contrib.auth import authenticate, login
from users.service import send_email_for_verify
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator as token_generator


User = get_user_model()

class LoginView(BaseLoginView):
    form_class = UserAuthenticationForm

class LogoutView(BaseLogoutView):
    template_name = 'users/logout.html'

class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('catalog:index')
        return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

class RegistrView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    # success_url = reverse_lazy('users:login')

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user=form.save()
            # user.is_active = False
            user.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)
            return redirect('users:confirm_email')
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
