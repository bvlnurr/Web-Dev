import { Component, Input, OnInit } from '@angular/core';
import { VacancyService } from '../services/vacancy.service';
import { Vacancy } from '../models/vacancy';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.css'],
  imports: [CommonModule]
})
export class VacancyListComponent implements OnInit {
  @Input() companyId!: number;
  vacancies: Vacancy[] = [];
  companies: any;

  constructor(private vacancyService: VacancyService) { }

  ngOnInit(): void {
    if (this.companyId) {
      this.vacancyService.getVacanciesByCompany(this.companyId)
        .subscribe(vacancies => {
          this.vacancies = vacancies;
        });
    }
  }
  getCompanyName(companyId: number): string {
    const company = this.companies.find((c: { id: number; }) => c.id === companyId);
    return company ? company.name : 'Unknown Company';
  }
}