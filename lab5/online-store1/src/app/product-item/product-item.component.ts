import { Component, Input } from '@angular/core';
import { Product } from '../models';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrl: './product-item.component.css'
})
export class ProductItemComponent {
  @Input() product!: Product;

  likeProduct() {
    this.product.likes++;
  }
}
