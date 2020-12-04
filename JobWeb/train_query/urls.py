from django.urls import path

from . import views

app_name = 'train_company'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.find_company_by_company_id, name = 'find_company_by_company_id'),
    path('<int:pk>/', views.find_company_by_company_name, name = 'find_company_by_company_name'),
    path('position/<int:pk>/', views.find_position_by_position_id, name = 'find_position_by_position_id'),
    path('position_commit/<int:temp_position_id>/', views.commit_resume, name = 'commit_resume'),
    path('train_company_search/', views.TrainCompanySearchView.as_view(), name = 'train_company_search'),
   
]