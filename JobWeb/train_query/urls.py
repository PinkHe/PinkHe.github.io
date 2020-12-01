from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.find_company_by_company_name, name = 'find_company_by_company_name'),
]