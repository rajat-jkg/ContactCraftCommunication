from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render , redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.db import connection
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html', {'homeActive': 'active'})



class loginView(LoginView):
    template_name = 'account/login.html'
    extra_context = {'accountActive': 'active'}
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if (self.request.user.is_authenticated):
            return redirect('account') 
        
        else:
            return super().get(request, *args, **kwargs)
    
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            connection.connection.ping()
            return super().post(request, *args, **kwargs)
        except Exception:
            connection.close()
            return super().post(request, *args, **kwargs)

class registerView(CreateView):
    form_class = UserCreationForm
    extra_context = {'accountActive': 'active'}
    template_name = 'account/register.html'
    success_url = '/account'
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if (self.request.user.is_authenticated):
            return redirect('home')
        return super().get(request, *args, **kwargs)
    
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            connection.connection.ping()
            return super().post(request, *args, **kwargs)
        except Exception:
            connection.close()
            return super().post(request, *args, **kwargs)


class Logout(LogoutView):
    template_name = 'account/logout.html'
    success_url = '/'
    extra_context = {'accountActive':'active'}
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            connection.connection.ping()
            return super().post(request, *args, **kwargs)
        except Exception:
            print("Exception", str(Exception))
            connection.close()
            return super().post(request, *args, **kwargs)


def account(request):
    connection.close()
    return render(request, 'account/account.html', {'accountActive':'active'})

@login_required
def update_user(request):
    if request.method == 'POST':
        connection.close()
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = UserUpdateForm(instance=request.user)
    connection.close()
    return render(request, 'account/update-profile.html', {'form': form})


class UpdatePassword(PasswordChangeView):
    form = PasswordChangeForm
    extra_context = {'accountActive': 'active'}
    template_name = 'account/password-change.html'
    def get_success_url(self) -> str:
        return '/account'
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            connection.ping()
            return super().post(request, *args, **kwargs)
        
        except Exception:
            connection.close()
            return super().post(request, *args, **kwargs)



class PasswordReset(PasswordResetView):
    template_name = 'account/password-reset/password-reset.html'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            connection.ping()
            return super().post(request, *args, **kwargs)
        
        except Exception:
            connection.close()
            return super().post(request, *args, **kwargs)



class PasswordResetDone(PasswordResetDoneView):
    template_name = 'account/password-reset/password-reset-done.html'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            connection.ping()
            return super().post(request, *args, **kwargs)
        
        except Exception:
            connection.close()
            return super().post(request, *args, **kwargs)


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'account/password-reset/password-reset-confirm.html'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            connection.ping()
            return super().post(request, *args, **kwargs)
        
        except Exception:
            connection.close()
            return super().post(request, *args, **kwargs)



class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'account/password-reset/password-reset-complete.html'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            connection.ping()
            return super().post(request, *args, **kwargs)
        
        except Exception:
            connection.close()
            return super().post(request, *args, **kwargs)

