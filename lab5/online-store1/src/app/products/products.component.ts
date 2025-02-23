import { Component } from '@angular/core';

@Component({
  selector: 'app-products',
  imports: [],
  templateUrl: './products.component.html',
  styleUrl: './products.component.css'
})
export class ProductsComponent {
  products = [
    {
      image: 'https://kaspi.kz/example1.jpg',
      name: 'iPhone 13',
      description: 'Apple iPhone 13 с 128GB памяти.',
      rating: 4.8,
      link: 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-12345678/'
    },
    {
      image: 'https://kaspi.kz/example2.jpg',
      name: 'Samsung Galaxy S22',
      description: 'Флагманский смартфон Samsung.',
      rating: 4.7,
      link: 'https://kaspi.kz/shop/p/samsung-galaxy-s22-256gb-12345678/'
    },
    {
      image: 'https://kaspi.kz/example3.jpg',
      name: 'MacBook Air M2',
      description: 'Лёгкий и мощный ноутбук Apple.',
      rating: 4.9,
      link: 'https://kaspi.kz/shop/p/macbook-air-m2-256gb-12345678/'
    },
    {
      image: 'https://kaspi.kz/example4.jpg',
      name: 'PlayStation 5',
      description: 'Консоль нового поколения от Sony.',
      rating: 4.9,
      link: 'https://kaspi.kz/shop/p/playstation-5-12345678/'
    },
    {
      image: 'https://kaspi.kz/example5.jpg',
      name: 'Xiaomi Redmi Note 12',
      description: 'Бюджетный смартфон с хорошими характеристиками.',
      rating: 4.6,
      link: 'https://kaspi.kz/shop/p/xiaomi-redmi-note-12-128gb-12345678/'
    },
    {
      image: 'https://kaspi.kz/example6.jpg',
      name: 'iPad Pro 11"',
      description: 'Планшет с мощным процессором M2.',
      rating: 4.9,
      link: 'https://kaspi.kz/shop/p/ipad-pro-11-256gb-12345678/'
    },
    {
      image: 'https://kaspi.kz/example7.jpg',
      name: 'Sony WH-1000XM5',
      description: 'Флагманские наушники с шумоподавлением.',
      rating: 4.8,
      link: 'https://kaspi.kz/shop/p/sony-wh-1000xm5-12345678/'
    },
    {
      image: 'https://kaspi.kz/example8.jpg',
      name: 'Samsung Galaxy Watch 5',
      description: 'Умные часы с расширенным функционалом.',
      rating: 4.7,
      link: 'https://kaspi.kz/shop/p/samsung-galaxy-watch-5-12345678/'
    },
    {
      image: 'https://kaspi.kz/example9.jpg',
      name: 'GoPro HERO11',
      description: 'Экшн-камера для самых смелых приключений.',
      rating: 4.8,
      link: 'https://kaspi.kz/shop/p/gopro-hero11-12345678/'
    },
    {
      image: 'https://kaspi.kz/example10.jpg',
      name: 'Dyson V15 Detect',
      description: 'Беспроводной пылесос с лазерной подсветкой.',
      rating: 4.9,
      link: 'https://kaspi.kz/shop/p/dyson-v15-detect-12345678/'
    }
  ];
  share(link: string) {
    window.open(`https://wa.me/?text=${encodeURIComponent(link)}`, '_blank');
  }
}
