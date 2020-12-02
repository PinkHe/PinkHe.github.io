from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:input_company_id>/', views.find_company_by_company_id, name = 'find_company_by_company_id'),
    path('<int:input_company_name>/', views.find_company_by_company_name, name = 'find_company_by_company_name'),
    path('<int:input_position_id>/', views.find_position_by_position_id, name = 'find_position_by_position_id'),
   
]