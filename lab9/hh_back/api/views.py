from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company,Vacancy

def companies_list(req):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json,safe=False)

def get_company(req, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=400)
    return JsonResponse(company.to_json())

def company_vacancy(req,id):
    try:
        vacancies_json = []
        company = Company.objects.get(id=id)
        for vacancy in Vacancy.objects.filter(company_id=int(id)):
            obj = vacancy.to_json()
            vacancies_json.append(obj) 
    except Company.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=400)
    return JsonResponse(vacancies_json, safe=False)

def vacancy_list(req):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vac.to_json() for vac in vacancies]
    return JsonResponse(vacancies_json,safe=False)

def get_vacancy(req,id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=400)
    return JsonResponse(vacancy.to_json())

def top_vacancy(req):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vac.to_json() for vac in vacancies]
    sorted_vacs = sorted(vacancies_json, key=lambda x: x["salary"], reverse=True)
    return JsonResponse(sorted_vacs,safe=False)
