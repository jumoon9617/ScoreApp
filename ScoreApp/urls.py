"""
URL configuration for ScoreApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from urllib import request
from django.contrib import admin
from django.urls import path, include
from app.urls import router
from app.views import process_json_data, get_score_player_data

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api_data/', include(router.urls)),
    path(r'api/process_json_data/', process_json_data),
    path(r'api/get_score_and_player/', get_score_player_data),
]
