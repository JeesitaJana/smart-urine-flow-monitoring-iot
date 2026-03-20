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
from sensor.views import home, dashboard, control_page, receive_data, get_valve_state

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('control/', control_page, name='control'),
    path('receive-data/', receive_data, name='receive_data'),
    path('valve-state/', get_valve_state, name='valve_state'),
]
