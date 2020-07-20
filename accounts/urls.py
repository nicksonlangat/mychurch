from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="login"
    ),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
]