from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('your-name/', views.get_name, name='your-name'),
    path('thanks/', views.thanks, name="thanks"),
    path('login/', views.login_user, name="login"),
]