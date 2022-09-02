
from django.contrib import admin
from django.urls import path, include
from users.views import login_request

urlpatterns = [
    path('', login_request, name='home'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('Servicios.urls')),
    path('users/', include('users.urls'))
]
