"""game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from player.views import create_player
from team.views import  create_team,edit_team,delete_team


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-player/', create_player,name="create-player"),
    path('add-team/', create_team, name="create-team"),
    path('edit-team/<int:pk>', edit_team, name="edit-team"),
    path('delete-team/<int:teamid>/<int:playerid>', delete_team, name="delete-team"),
]

