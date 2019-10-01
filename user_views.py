from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.post)
    if form.is_valid():
      form.save()
  else:
    form = RegistrationForm()
  
  context = {'form':form}
  return render(request, 'user/register.html', context)
  
  
  ###################################### urls.py for the user model #####################################
  
  from django.urls import path
  from . import views
  from django.contrib.auth import views as auth_views
  
  urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html' name='logout'),
    ]
    
    
