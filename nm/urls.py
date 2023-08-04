"""
URL configuration for nm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
]

# python -m venv .venv
# .\.venv\Scripts\Activate.ps1
# pip install django
# python manage.py runserver
# pip freeze >> requirements.txt
# pip install -r .\requirements.txt
# Ctrl + C -> Break terminal

# Alt + Shift
# Ctrl + D
# Alt + Arrow (Up, Down)
