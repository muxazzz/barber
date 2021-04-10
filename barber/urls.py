from django.urls import path
from .views import AuthorEdit, login
from . import views
app_name = 'barber'

urlpatterns = [
    path('thanks', views.index, name='index'),
    path('', AuthorEdit.as_view(), name='author_create'), 
    path('login/', login, name='login')
]