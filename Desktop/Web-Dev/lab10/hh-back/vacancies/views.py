from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Vacancy
from .serializers import VacancySerializer
from companies.models import Company

# Function-based views
@api_view(['GET', 'POST'])
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vacancy_detail(request, pk):
    try:
        vacancy = Vacancy.objects.get(pk=pk)
    except Vacancy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VacancySerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    vacancies = company.vacancies.all()
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)

# Class-based views
class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VacancyDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist:
            return None

    def get(self, request, pk):
        vacancy = self.get_object(pk)
        if not vacancy:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, pk):
        vacancy = self.get_object(pk)
        if not vacancy:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VacancySerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vacancy = self.get_object(pk)
        if not vacancy:
            return Response(status=status.HTTP_404_NOT_FOUND)
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CompanyVacanciesAPIView(APIView):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        vacancies = company.vacancies.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)