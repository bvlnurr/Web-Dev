import { Component, Input } from '@angular/core';
import { Product } from '../models';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css'
})
export class ProductListComponent {
  @Input() products: Product[] = [];
}
