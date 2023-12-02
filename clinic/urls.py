from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nomapp.urls')),
    path('auth/', include('authentificationn.urls')),  # Use a specific path like 'auth/'
]

# Your authentificationn.urls remains the same
