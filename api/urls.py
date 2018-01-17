from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('catalog.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
]
