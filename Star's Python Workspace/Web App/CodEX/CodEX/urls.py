"""CodEX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from search import views as search_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_views.search),
    path('nls/', search_views.nlsindex),
    path('nls-result/', search_views.nls_result),
    path('snippet/', search_views.plagiarize),
    path('snippet-result/', search_views.plagiarizeResult),
    path('snippet-detail/', search_views.snippet_detail),
    path('detail/', search_views.detail),
    path('init/', search_views.init),
    path('', search_views.index),
]
