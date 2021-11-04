


class Cart:
    
    def _init_(self, price, item_name, quantity, total):
        self.item_name = item_name 
        self.price = price
        self.quatintiy = quantity
        self.total = total
    
    def add_item(self, amount, price, quantity):
        self.total = (quantity * price)
        self.quantity += amount
    
    def remove_item(self, amount, quantity, item_name):
        self.total -= (quantity )
        if quantity > self.item_name[item_name]:
            del self.item_name
        self.item[item_name] -= quantity

    def checkout(self, cash_paid):
        balance = 0
        if cash_paid < self.total:
            return "Need more cash to check out"
        balance = cash_paid - self.total
        return balance
    

class Russ(Cart):
    def _init_(self, price, item_name, quantity, total):
        return super()._init_(price, item_name, quantity, total)

    def checkcart(self):
        return Russ(Cart)

my_cart = Russ(4, "chicken", 4, 16)

print(''' ***SHOPPING CART***

        Select a number to choose what you want to do:

        1. View cart
        2. Add items to cart
        3. Remove item from cart
        4. Checkout
        ''')
      



checkcart = False

while not checkcart :

        Cart


        choice = input("What would you like to do with your cart")



        if choice == "1":
            my_cart.checkcart
        elif choice == "2":
            my_cart.add_item()
        elif choice == "3":
            my_cart.remove_item()
        elif choice =="4":    
            my_cart.checkout()
        else:
            done = True




