from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import AddForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from django.views.generic import CreateView
from .models import ContactForm
# Create your views here.

def dashboard(request):
    try:
        connection.ping()
    except Exception as E:
        connection.close()
    finally:
        formList = enumerate(ContactForm.objects.filter(user = request.user))
        return render(request, 'dashboard.html', {'dashboardActive': 'active', 'formList': formList, 'sr':1})
    


class AddNewForm(CreateView):
    model = ContactForm
    template_name = 'create-form.html'
    form_class = AddForm
    success_url = '/forms/dashboard'
    login_url = '/login'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            connection.ping()
        except Exception as E:
            connection.close()
        finally:
            return super().post(request, *args, **kwargs)
        
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            connection.ping()
        except Exception as E:
            connection.close()
        finally:
            return super().get(request, *args, **kwargs)