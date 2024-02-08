"""
URL configuration for multishop_project project.

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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name = 'index.html'), name='home'),
    path('cart/', TemplateView.as_view(template_name = 'cart.html'), name='cart'),
    path('checkout/', TemplateView.as_view(template_name = 'checkout.html'), name='checkout'),
    path('contact/', TemplateView.as_view(template_name = 'contact.html'), name='contact'),
    path('detail/', TemplateView.as_view(template_name = 'detail.html'), name='detail'),
    path('shop/', TemplateView.as_view(template_name = 'shop.html'), name='shop'),
    re_path(r'^accounts/',include('django.contrib.auth.urls')),

]
