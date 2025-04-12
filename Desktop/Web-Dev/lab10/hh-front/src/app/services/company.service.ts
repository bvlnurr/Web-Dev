import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { Company, Vacancy } from '../models/company';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  private apiUrl = 'http://localhost:8000/api/';

  constructor(private http: HttpClient) { }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.apiUrl}companies/`);
  }

  getCompanyVacancies(companyId: number): Observable<Vacancy[]> {
    // Измените URL на тот, что использует ваш бэкенд
    return this.http.get<Vacancy[]>(`${this.apiUrl}vacancies/by_company/${companyId}/`);
  }
}