import { Component } from '@angular/core';
import { Category, Product } from './models';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  categories: Category[] = [
    {
      name: 'Смартфоны',
      products: [
        { id: 1, name: 'iPhone 13', description: 'Apple iPhone 13', price: 399000, likes: 0, image: 'https://kaspi.kz/example1.jpg' },
        { id: 2, name: 'Samsung S22', description: 'Флагман Samsung', price: 350000, likes: 0, image: 'https://kaspi.kz/example2.jpg' },
        { id: 3, name: 'Xiaomi Redmi Note 12', description: 'Бюджетный смартфон', price: 150000, likes: 0, image: 'https://kaspi.kz/example5.jpg' },
        { id: 4, name: 'Google Pixel 7', description: 'Фирменный Google', price: 300000, likes: 0, image: 'https://kaspi.kz/example6.jpg' },
        { id: 5, name: 'OnePlus 10', description: 'Флагман OnePlus', price: 280000, likes: 0, image: 'https://kaspi.kz/example7.jpg' }
      ]
    },
    {
      name: 'Ноутбуки',
      products: [
        { id: 6, name: 'MacBook Air M2', description: 'Ноутбук Apple', price: 700000, likes: 0, image: 'https://kaspi.kz/example3.jpg' },
        { id: 7, name: 'Asus ROG Strix', description: 'Игровой ноутбук', price: 600000, likes: 0, image: 'https://kaspi.kz/example4.jpg' },
        { id: 8, name: 'HP Pavilion', description: 'Бюджетный ноутбук', price: 350000, likes: 0, image: 'https://kaspi.kz/example8.jpg' },
        { id: 9, name: 'Lenovo Legion', description: 'Игровой Lenovo', price: 550000, likes: 0, image: 'https://kaspi.kz/example9.jpg' },
        { id: 10, name: 'Dell XPS 13', description: 'Ультрабук Dell', price: 650000, likes: 0, image: 'https://kaspi.kz/example10.jpg' }
      ]
    }
  ];
  selectedCategory: Category | null = null;

  selectCategory(category: Category) {
    this.selectedCategory = category;
  }
}
