# Michael Perrine
# DSC 510
# Week 11
# Programming Assignment
# Author Michael Perrine
# 11/08/24

import locale


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# this establishes the class for the register program,
class CashRegister:


# This variable will be used to count the number of items
    items_in_cart = 0

#This function will call the items and keep track of items in cart


    def __init__(self):
        self.totalprice = 0.0
        self.items_in_cart = 0

    def additem(self, price):
        self.totalprice = price
        self.items_in_cart +=1

# This will return the total price

    def get_total(self):
        return self.totalprice

# This will return the total count in cart

    def get_count(self):
        return self.items_in_cart






def main():

    print("Hello welcome to My Store")

basket = CashRegister

# This will give the user the ability to add prices for the register

while True:
        grocery = input("Please add the cost of the grocery item. Please enter (q or quit) when finished. \n")

        if grocery.lower() == "q" or grocery == "quit":
            break

# This will validate user response and convert to a floating point integer

        try:
            price = float(grocery)

            if price <= 0:
                print("Invalid price, Please try again")

            else:
                basket.additem(price)

                print(f"Item added!!: {locale.currency(price, grouping = True)}")

# This will execute when an invalid response is entered
        except ValueError:
            print("Invalid input please try again")


print(f"Total number of items in your cart: {basket.get_count()}")

print(f"Thank you for shopping with us, Your total is: {locale.currency(basket.get_total())}")

print("Thank you for shopping with us. Please come back soon")

if __name__==__main__:
    main()






























