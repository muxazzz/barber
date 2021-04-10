from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth 
from .forms import OrderForm
from django.http import HttpResponseRedirect
from .models import Order  
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm 


def index(request):
    return HttpResponse("Спасибо! Ваш заказ успешно создан. Администратор свяжется с Вами в ближайшее время.")

def login(request):  
    if request.method == 'POST':  
        form = AuthenticationForm(request=request, data=request.POST)  
        if form.is_valid():  
            auth.login(request, form.get_user())  
            server_ips = [i.client_name for i in Order.objects.all()]
      

    # прообраз личного кабинета
    # # Render list page with the documents and the form
    #     return render(request, 'index.html',
    #     {'Order': server_ips, 'username': request.user.username})

    # else:  
    #     context = {'form': AuthenticationForm()}  
    #     return render(request, 'login.html', context)  
        
class AuthorEdit(CreateView):  
    model = Order  
    form_class = OrderForm  
    success_url = 'http://www.helena.ru.com/thanks'
    template_name = 'index.html'  