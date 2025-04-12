import { Component, OnInit } from '@angular/core';
import { CompanyService } from '../services/company.service';
import { Company, Vacancy } from '../models/company';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css'],
  standalone: true,
  imports: [CommonModule]
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];
  selectedCompanyId: number | null = null;
  vacancies: Vacancy[] = [];
  loading = false;
  error: string | null = null;

  constructor(private companyService: CompanyService) {}

  ngOnInit(): void {
    this.loadCompanies();
  }

  loadCompanies(): void {
    this.companyService.getCompanies().subscribe({
      next: (data) => this.companies = data,
      error: (err) => this.error = 'Failed to load companies'
    });
  }

  showVacancies(companyId: number): void {
    this.selectedCompanyId = companyId;
    this.loading = true;
    this.error = null;
    
    this.companyService.getCompanyVacancies(companyId).subscribe({
      next: (data) => {
        this.vacancies = data;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Failed to load vacancies';
        this.loading = false;
      }
    });
  }
}