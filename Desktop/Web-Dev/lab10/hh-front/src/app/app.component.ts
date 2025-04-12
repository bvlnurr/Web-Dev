import { Component } from '@angular/core';
import { CompanyListComponent } from './company-list/company-list.component';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [CommonModule, CompanyListComponent]
})
export class AppComponent {
  title = 'hh-front';
}