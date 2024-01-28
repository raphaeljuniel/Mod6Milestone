#This code is borrowed from mod 4
class ItemToPurchase:          #creates the name of the class
	def __init__(item, name, price, quantity, description):     # defines the attributes for the objects of the class. Description is newly added.
		item.name = name
		item.price = price
		item.quantity = quantity
		item.description = description
        
class ShoppingCart: #Creates a class called ShoppingCart.
    def __init__(self, customer_name = "none", date = "January 1, 2020"): #defines the initial variables given to the ShoppingCart class
        self.customer_name = customer_name #creates a customer name attribute.
        self.date = date #creates a date attribute
        self.cart_items = [] #creates a list that will store the items of the cart.

    def add_item(self, ItemToPurchase): #Defines a function that will add an ItemToPurchase object to the cart. Currently not implemented.
            self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name): #Defines a function that will remove an item from the cart using its name.
        for item in self.cart_items: #checks every item in the current ShoppingCart.cart_items
            if item.name == item_name: #Checks if the item name is in the cart_items
                self.cart_items.remove(item) #removes the item's name if it is found.
            else: #tells the progam what to do if the item was not found.
                print("Item not found in cart. Nothing removed.") #Lets the user know their item was not found in the cart.
            #exits the program

    def modify_item(self, ItemToPurchase): #Defines a function that will allow items to be modified from the cart.
                #Currently unimplemented
                pass

    def get_num_items_in_cart(self): #Defines a function that get the number of items in the cart.
        return sum(item.quantity for item in self.cart_items) #Checks the quantity of items for each item in the cart and returns the sum to the user.

    def get_cost_of_cart(self): #Defines a function that will get the cost of each item in the cart.
        return sum(item.price * item.quantity for item in self.cart_items) #Calculates the cost of each item in the cart by multiplying the item's price by its quantity.
                                                                           #Then sums the total for all items.

    def print_total(self): #Defines a function that will print the total cost of the cart.
        if not self.cart_items: #Checks if the cart does not have an item
            print("SHOPPING CART IS EMPTY") #Tells the user the cart is empty
            
        else: #tells the computer what to do if the cart is not empty
            total_cost = self.get_cost_of_cart() #defines a variable called total_cost which gets its value from get_cost_of_cart
            print(f"{self.customer_name}'s Shopping Cart - {self.date}") #prints the user's name and date.
            print(f"Number of items: {self.get_num_items_in_cart()}") #prints the number of items in the cart using a previous function.
            for item in self.cart_items: #iterates through every item in cart_items
                print(f"{item.name} {item.quantity} @ ${item.price} = {item.quantity * item.price}") #Prints the item's name, quantity, and price, then tells the user the total for that item.
            print(f"Total:") #Tells the user their total will be below.
            return total_cost            
    
    def print_descriptions(self): #Defines a function that will print out the description of each item.
        print(f"{self.customer_name}'s Shopping Cart - {self.date}") #prints the name and date of the user
        print("Item Descriptions") #prints "Item Descriptions"
        for item in self.cart_items: #iterates through every item in cart_items
            print(f"{item.name}: {item.description}") #prints the item's names and descriptions
            
          
def print_menu(Cart):
    allow_loop = True #Creates a boolean variable for the loop
    while allow_loop == True: #Creates a while loop that will continuously repeat the bellow code.
        #The bellow code prints out the menu formatting.
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        
        user_choice = str(input("\nChoose an option:")) #defines a variable called user choice which takes the user's input for the menu.
        if user_choice.lower() == "q": #checks if the user input q
            allow_loop = False #ends the program loop
            
        elif user_choice.lower() == "o": #Checks if the user input o
            print("\nOUTPUT SHOPPING CART") #lets the user know they are in the Output shopping cart menu option.
            print(Cart.print_total()) #Will print the user's name, date, number of items, each item and its quantity and price, and the total cost of the cart.
            
        elif user_choice.lower() == "i": #Checks if the user input i
            print(Cart.print_descriptions()) #Prints the item's descriptions from the function previously written.
        
        else: #Tells the computer what to do if the an improper variable is provided.
            print("An invalid option was given. Please try again.")
            
#Creating a test case for the code to run
#Each ItemToPurchase object has a name, price, quantity, description
Apple = ItemToPurchase("Apple", 1.31, 3, "Just an apple")
Figurine = ItemToPurchase("Figurine", 30.32, 1, "It calmly spins on its small stand.")
Comalone = ItemToPurchase("Comalone", 15.51, 3, "Used to move around logs.")

Raphaels_Cart = ShoppingCart("Raphael Juniel", "January 28, 2024",)
Raphaels_Cart.add_item(Apple)
Raphaels_Cart.add_item(Figurine)
Raphaels_Cart.add_item(Comalone)

print_menu(Raphaels_Cart)
