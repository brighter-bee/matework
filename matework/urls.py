"""matework URL Configuration

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
from django.urls import path, include
import profiles.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", profiles.views.index),
    path('<int:person_id>', profiles.views.person),
    path('profile/<str:request_username>', profiles.views.profile),
    #  path('profile/<str:username>/edit', profiles.views.profile_edit),
    path("signup/", user.views.signup, name="signup"),
    path("", include("django.contrib.auth.urls")),
]
