from django.urls import path
from users.views import login_request, registrar
from django.contrib.auth.views import LogoutView

urlpatterns=[
path ("login/", login_request, name="login"),
path ("registrar/", registrar, name="registrar"),
path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),

]