from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from .views import UserViewSet


urlpatterns = [
    path('employees', UserViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('employees/<str:pk>',UserViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',

    }))

]