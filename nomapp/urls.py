from django.conf import settings
from django.urls import path
from nomapp import views
from .views import Home 
from .models import DoctorAvailability
from .views import trigger_notification


from django.conf.urls.static import static
urlpatterns = [
     path('', views.Home ,name ="home"),
     path('trigger-notification/', trigger_notification, name='trigger-notification'),

     path('search_doctors', views.search_doctors,name ="search_doctors"),
     path('doctors.html/', views.Doctors ,name ="Doctors"),
     path('services.html/', views.Services ,name ="Services"),
     path('about.html/', views. About ,name ='about'),
     path('blog.html/', views.Blog, name='blog'),
     path('contact.html/', views.Contact ,name ="contact"),]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


