class Product:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Availability: {self.availability}"
    

class Cart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product):
        self.cart.remove(product)

    def update_product(self, product, new_product):
        self.cart.remove(product)
        self.cart.append(new_product)

    def total_bill(self):
        total = 0
        for product in self.cart:
            total += product.price
        return total

    def __str__(self):
        return f"Cart: {self.cart}"
    

class Products:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def update_product(self, product, new_product):
        self.products.remove(product)
        self.products.append(new_product)

    def __str__(self):
        return f"Products: {self.products}"
    


if __name__ == "__main__":
    cart = Cart()
    products = Products()
    while 1:
        print("Welcome to the E-commerce cart system!")
        print("What would you like to do?")
        print("1. Display a list of products with their attributes.")
        print("2. Add products to the Store.")
        print("3. Add products to the cart.")
        print("4. Update quantities of products in the cart.")
        print("5. Remove products from the cart.")
        print("6. Calculate and display the total bill.")
        print("7.Remove products from the Store.")
        print("8. Exit.")
        option = (input("Enter your option: "))
        try:
            option = int(option)
        except ValueError:
            print("Please enter a valid option.")
            continue
        if option == 1:
            print("Displaying a list of products with their attributes.")
            for product in products.products:
                print(product)
        elif option == 2:
            print("Enter the product details:")
            name = input("Name: ")
            price = input("Price: ")
            avail = input("Availability: (1/0)")
            if len(name) == 0 or len(price) == 0 or len(avail) == 0:
                print("Please enter valid details.")
                continue
            try:
                price = int(price)
            except ValueError:
                print("Please enter a valid price.")
                continue
            try:
                avail = int(avail)
            except ValueError:
                print("Please enter a valid availability.")
                continue
            avail = int(avail)
            #print(type(avail))
            # TypeError: '<' not supported between instances of 'builtin_function_or_method' and 'int'
            if avail < 0 or avail > 1:
                print("Please enter a valid availability.")
                continue
            if avail == 1:
                avail = True
            else:
                avail = False
            if price < 0:
                print("Please enter a valid price.")
                continue

            product = Product(name, price, avail)
            products.add_product(product)
            print("Product added successfully!")
        
        elif option == 3:
            print("Adding products to the cart.")
            for product in products.products:
                print(product)
            name = input("Enter the name of the product you want to add to the cart: ")
            for product in products.products:
                if product.name == name:
                    cart.add_product(product)
                    print("Product added to the cart successfully!")
                    break
            else:
                print("Product not found.")
        elif option == 4:
            print("Updating quantities of products in the cart.")
            for product in cart.cart:
                print(product)
            name = input("Enter the name of the product you want to update: ")
            for product in cart.cart:
                if product.name == name:
                    quantity = input("Enter the new quantity: ")
                    try:
                        quantity = int(quantity)
                    except ValueError:
                        print("Please enter a valid quantity.")
                        continue
                    for i in range( quantity):
                        cart.add_product(Product(product.name, product.price, True))
                    print("Product updated successfully!")
                    break
            else:
                print("Product not found.")
        elif option == 5:
            print("Removing products from the cart.")
            print(cart)
            name = input("Enter the name of the product you want to remove: ")
            for product in cart.cart:
                if product.name == name:
                    cart.remove_product(product)
                    print("Product removed successfully!")
                    break
            else:
                print("Product not found.")
        elif option == 6:
            print("Calculating and displaying the total bill.")
            print(cart)
            print(f"Total bill: {cart.total_bill()}")
        elif option == 7:
            print("Removing products from the Store.")
            for product in products.products:
                print(product)
            name = input("Enter the name of the product you want to remove: ")
            for product in products.products:
                if product.name == name:
                    products.remove_product(product)
                    print("Product removed successfully!")
                    break
            else:
                print("Product not found.")
        else:
            print("Exiting...")
            break
        input("Press Enter to continue...")

# Written by Golla Harshith
