class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.product_id}. {self.name} - ₹{self.price:.2f} (Stock: {self.stock})"


class ShoppingCart:
    def __init__(self):
        # Dictionary to store product_id as key and details as value
        self.items = {}

    def add_item(self, product, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        
        if quantity > product.stock:
            print(f"Sorry, only {product.stock} units of {product.name} available in stock.")
            return

        if product.product_id in self.items:
            new_qty = self.items[product.product_id]['quantity'] + quantity
            if new_qty > product.stock:
                print(f"Cannot add more. Total would exceed available stock ({product.stock}).")
                return
            self.items[product.product_id]['quantity'] = new_qty
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}
        print(f"Successfully added {quantity} x {product.name} to your cart.")

    def remove_item(self, product_id):
        if product_id in self.items:
            removed = self.items.pop(product_id)
            print(f"Removed {removed['product'].name} from your cart.")
        else:
            print("Item not found in your cart.")

    def view_cart(self):
        if not self.items:
            print("\nYour shopping cart is currently empty.")
            return False
        
        print("\n--- YOUR SHOPPING CART ---")
        print(f"{'ID':<5} | {'Product Name':<20} | {'Price':<10} | {'Qty':<5} | {'Total':<10}")
        print("-" * 65)
        subtotal = 0
        for item_data in self.items.values():
            prod = item_data['product']
            qty = item_data['quantity']
            total = prod.price * qty
            subtotal += total
            print(f"{prod.product_id:<5} | {prod.name:<20} | ₹{prod.price:<9.2f} | {qty:<5} | ₹{total:<9.2f}")
        print("-" * 65)
        print(f"Subtotal: ₹{subtotal:.2f}")
        return True

    def checkout(self):
        if not self.items:
            print("Your cart is empty. Add some items before checking out.")
            return False
        
        self.view_cart()
        tax_rate = 0.05  # 5% tax/GST example
        subtotal = sum(item['product'].price * item['quantity'] for item in self.items.values())
        tax_amount = subtotal * tax_rate
        grand_total = subtotal + tax_amount

        print(f"\nTax (5%): ₹{tax_amount:.2f}")
        print(f"Grand Total: ₹{grand_total:.2f}")
        
        confirm = input("\nConfirm order? (y/n): ").strip().lower()
        if confirm == 'y':
            # Deduct stock
            for item_data in self.items.values():
                prod = item_data['product']
                qty = item_data['quantity']
                prod.stock -= qty
            print("\nOrder placed successfully! Thank you for shopping with us.")
            self.items.clear()
            return True
        else:
            print("Checkout cancelled.")
            return False


class Store:
    def __init__(self):
        self.catalog = {
            1: Product(1, "Wireless Mouse", 799.00, 15),
            2: Product(2, "Mechanical Keyboard", 2499.00, 8),
            3: Product(3, "USB-C Hub", 1299.00, 12),
            4: Product(4, "Gaming Headset", 1899.00, 10),
            5: Product(5, "Laptop Stand", 999.00, 20)
        }
        self.cart = ShoppingCart()

    def display_catalog(self):
        print("\n--- AVAILABLE PRODUCTS ---")
        for prod in self.catalog.values():
            print(prod)
        print("-" * 30)

    def run(self):
        while True:
            print("\n=== ONLINE SHOPPING SYSTEM ===")
            print("1. View Products")
            print("2. Add Item to Cart")
            print("3. View Cart")
            print("4. Remove Item from Cart")
            print("5. Checkout")
            print("6. Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                self.display_catalog()
            elif choice == '2':
                self.display_catalog()
                try:
                    pid = int(input("Enter Product ID to add: "))
                    if pid in self.catalog:
                        qty = int(input("Enter quantity: "))
                        self.cart.add_item(self.catalog[pid], qty)
                    else:
                        print("Invalid Product ID.")
                except ValueError:
                    print("Please enter valid numeric values for ID and quantity.")
            elif choice == '3':
                self.cart.view_cart()
            elif choice == '4':
                if self.cart.view_cart():
                    try:
                        pid = int(input("Enter Product ID to remove from cart: "))
                        self.cart.remove_item(pid)
                    except ValueError:
                        print("Please enter a valid numeric Product ID.")
            elif choice == '5':
                self.cart.checkout()
            elif choice == '6':
                print("\nThank you for visiting! Goodbye.")
                break
            else:
                print("Invalid choice! Please select between 1 and 6.")


if __name__ == "__main__":
    store = Store()
    store.run()