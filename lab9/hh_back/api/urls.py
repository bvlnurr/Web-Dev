from django.urls import path
from api.views import companies_list
from api.views import get_company
from api.views import company_vacancy
from api.views import get_vacancy
from api.views import vacancy_list
from api.views import top_vacancy

urlpatterns = [
    path('companies/',companies_list ),
    path('companies/<int:id>/', get_company),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:id>/', get_vacancy),
    path('companies/<int:id>/vacancies/', company_vacancy),
    path('vacancies/top_ten/',top_vacancy )
]
