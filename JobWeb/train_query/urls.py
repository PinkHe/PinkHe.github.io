from django.urls import path

from . import views

app_name = 'train_company'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'find_company_by_company_id'),
    # path('<int:pk>/', views.find_company_by_company_name, name = 'find_company_by_company_name'),
    # path('position/<int:pk>/', views.find_position_by_position_id, name = 'find_position_by_position_id'),
    # path('position_commit/<int:temp_position_id>/', views.commit_resume, name = 'commit_resume'),
   
]