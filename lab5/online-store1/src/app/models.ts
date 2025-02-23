export interface Product {
    id: number;
    name: string;
    description: string;
    price: number;
    likes: number;
    image: string;
  }
  
  export interface Category {
    name: string;
    products: Product[];
  }
  