from django.urls import path
from .views import RegisterView,test, test_auth


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('test/', test, name='test'),
    path('test-auth/', test_auth, name='auth_test'),
]