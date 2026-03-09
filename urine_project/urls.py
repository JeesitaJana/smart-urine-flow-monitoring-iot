"""
URL configuration for urine_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sensor.views import receive_data,home, dashboard, control_page, get_valve_state

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/',receive_data),
    path('', home),
    path('dashboard/',dashboard),
    path('control/', control_page),
    path('get_valve_state/', get_valve_state),
]
