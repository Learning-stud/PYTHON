class Pizzeria:
    def _init_(self):
        self.pizza_prices = {"1": 10.99, "2": 20.99, "3": 29.99}
        self.pasta_prices = {"1": 9.5, "2": 17.0, "3": 27.5}
        self.pizza_discount_trigger = 4
        self.pasta_discount_trigger = 4
        self.order_count = 0
        self.total_sales_pizza = 0
        self.total_sales_pasta = 0
        self.total_sales = 0
        self.soft_drinks_given = 0
        self.bruschetta_given = 0
        self.brownie_ice_cream_given = 0

    def display_menu(self):
        print("1 large pizza = 10.99 AUD\n2 large Pizzas = 20.99 AUD\n3 Large Pizzas = 29.99 AUD")
        print("**Buy 4 or more pizza and get 1.5lt of soft drink free**")
        print("1 large pasta = 9.5 AUD\n2 large pastas = 17.00 AUD\n3 large pastas = 27.50 AUD")
        print("***Buy 4 or more pastas and get 2 bruschetta free.***")
        print("***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.")

    def place_order(self, name):
        print(f"Welcome, {name}")
        pizza_qty = int(input("Enter number of pizza orders you want: "))
        pizza_amount = self.calculate_order_amount(pizza_qty, self.pizza_prices, self.pizza_discount_trigger)
        print(f"Your pizza order amount is: {pizza_amount:.2f}")
        if pizza_qty >= self.pizza_discount_trigger:
            print("**Congratulations!! 1.5lt soft drink free**")
            self.soft_drinks_given += 1

        pasta_qty = int(input("Enter number of pasta orders you want: "))
        pasta_amount = self.calculate_order_amount(pasta_qty, self.pasta_prices, self.pasta_discount_trigger)
        print(f"Your pasta order amount is: {pasta_amount:.2f}")
        if pasta_qty >= self.pasta_discount_trigger:
            print("**Congratulations!! Get 2 bruschetta free**")
            self.bruschetta_given += 2

        if pizza_qty + pasta_qty >= self.pizza_discount_trigger:
            print("**Congratulations!! Get 2 chocco brownies ice cream free**")
            self.brownie_ice_cream_given += 2

        total_order_amount = pizza_amount + pasta_amount
        print(f"Your total order is: {total_order_amount:.2f}\n")
        self.update_sales(total_order_amount)
        self.order_count += 1

    def calculate_order_amount(self, qty, prices, discount_trigger):
        if qty >= discount_trigger:
            return prices["1"] * qty * 0.9
        else:
            return prices[str(qty)]

    def update_sales(self, total_order_amount):
        self.total_sales += total_order_amount
        self.total_sales_pizza += total_order_amount / 2
        self.total_sales_pasta += total_order_amount / 2  

    def display_summary(self):
        print("\n----------- Pizza and Pasta Bill --------------")
        print(f"Payment received from pizza: {self.total_sales_pizza:.2f}")
        print(f"Payment received from pasta: {self.total_sales_pasta:.2f}")
        print(f"Payment received today: {self.total_sales:.2f}")
        print(f"Number of pizza and pasta sold in one shift: {self.order_count}")
        print(f"Number of 1.5lt soft drink bottles given: {self.soft_drinks_given}")
        print(f"Number of bruschetta given to customer: {self.bruschetta_given}")
        print(f"Number of chocco brownies ice cream given to customer: {self.brownie_ice_cream_given}\n")
        print("Bye Bye !!!")

# Main program
pizzeria = Pizzeria()
pizzeria.display_menu()

while True:
    proceed = input("Want to enter an order from another customer? (Y/N): ").upper()
    if proceed != 'Y':
        break
    else:
        customer_name = input("Enter your name: ")
        pizzeria.place_order(customer_name)

pizzeria.display_summary()