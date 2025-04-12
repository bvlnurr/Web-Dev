from django.urls import path
from . import views

urlpatterns = [
    # Function-based views
    path('', views.vacancy_list),
    path('<int:pk>/', views.vacancy_detail),
    path('by_company/<int:company_id>/', views.company_vacancies),
    
    # Class-based views
    path('cbv/', views.VacancyListAPIView.as_view()),
    path('cbv/<int:pk>/', views.VacancyDetailAPIView.as_view()),
    path('cbv/by_company/<int:company_id>/', views.CompanyVacanciesAPIView.as_view()),
]