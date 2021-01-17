from django.urls import path
from .views import RegisterView,test


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('test/', test, name='test'),
]