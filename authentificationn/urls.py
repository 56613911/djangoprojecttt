
from django.urls import path
from .views import CustomLoginView, register, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path('logout/', user_logout, name='logout'),
]