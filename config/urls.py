"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from khuthon import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('khuthon/', include('khuthon.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
    path('univBT/', views.univBT),
    path('comBT/', views.comBT),
    path('univBT/leftStudent/', views.leftStudent),
    path('univBT/leftUniv/', views.leftUniv),
    path('comBT/rightUniv/', views.rightUniv),
    path('comBT/rightEmp/', views.rightEmp),
    path('leftStudent/', views.leftStudent),
    path('leftUniv/', views.leftUniv),
    path('rightUniv/', views.rightUniv),
    path('rightEmp/', views.rightEmp),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
