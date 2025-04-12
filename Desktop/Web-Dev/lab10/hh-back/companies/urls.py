from django.urls import path
from . import views

urlpatterns = [
    # Function-based views
    path('', views.company_list),
    path('<int:pk>/', views.company_detail),
    
    # Class-based views
    path('cbv/', views.CompanyListAPIView.as_view()),
    path('cbv/<int:pk>/', views.CompanyDetailAPIView.as_view()),
]