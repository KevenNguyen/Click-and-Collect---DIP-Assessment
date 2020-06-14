import datetime

date_today = datetime.datetime.now()
day_today = date_today.strftime("%A")

foodmenu = {
    "Monday" : "$1: Fresh Fruit | Noodle Snack | Afghan Cookie \n$1.50: Hash Brown | Spaghetti Bun \n$2: Potato Chips | Popcorn | Chips | Garlic Bread | Sausage Roll | Water | Juicie | Moosie | Slushy | Calci Yum | Hot Chocolate \n$3: Pizza Bread | Brownie | Pizza | Quiche | Large Sausage Roll | Aloe Vera | \n$3.50: Steam Bun | Noodle Bowl \n$4: Chicken Sandwhich | Chicken Sub \n$4.50: Pie",
    
    "Tuesday" : "$1: Fresh Fruit | Noodle Snack | Afghan Cookie \n$1.50: Hash Brown | Spaghetti Bun \n$2: Potato Chips | Popcorn | Chips | Garlic Bread | Sausage Roll | Water | Juicie | Moosie | Slushy | Calci Yum | Hot Chocolate \n$3: Pizza Bread | Brownie | Pizza | Hot Dog | Large Sausage Roll | Aloe Vera | \n$3.50: Steam Bun | Noodle Bowl | Nachos \n$4: Chicken Sandwhich | Chicken Sub \n$4.50: Pie",
    
    "Wednesday" : "$1: Fresh Fruit | Noodle Snack | Afghan Cookie \n$1.50: Hash Brown | Spaghetti Bun \n$2: Potato Chips | Popcorn | Chips | Garlic Bread | Sausage Roll | Water | Juicie | Moosie | Slushy | Calci Yum | Hot Chocolate \n$3: Pizza Bread | Brownie | Pizza | Potato Puff | Large Sausage Roll | Aloe Vera | \n$3.50: Steam Bun | Noodle Bowl \n$4: Chicken Sandwhich | Chicken Sub \n$4.50: Pie",
    
    "Thursday" : "$1: Fresh Fruit | Noodle Snack | Afghan Cookie \n$1.50: Hash Brown | Spaghetti Bun \n$2: Potato Chips | Popcorn | Chips | Garlic Bread | Sausage Roll | Water | Juicie | Moosie | Slushy | Calci Yum | Hot Chocolate \n$3: Pizza Bread | Brownie | Pizza | Large Sausage Roll | Aloe Vera | \n$3.50: Steam Bun | Noodle Bowl \n$4: Chicken Sandwhich | Chicken Sub \n$4.50: Pie | Butter Chicken Wrap",
    
    "Friday" : "$1: Fresh Fruit | Noodle Snack | Afghan Cookie \n$1.50: Hash Brown | Spaghetti Bun \n$2: Potato Chips | Popcorn | Chips | Garlic Bread | Sausage Roll | Water | Juicie | Moosie | Slushy | Calci Yum | Hot Chocolate \n$3: Pizza Bread | Brownie | Pizza | Quiche | Large Sausage Roll | Aloe Vera | \n$3.50: Steam Bun | Noodle Bowl \n$4: Chicken Sandwhich | Chicken Sub \n$4.50: Pie | Sushi"
}

member_list = ["Keven", "Password123"]
cart_prices = []
cart_items = []

def account_log_reg():
    while True:
        login_signup = input("Please enter: | A for Login | B for Signup | ") .upper()
        if login_signup =="A":
            member_username = input("Please enter your username for Click and Collect program (case-sensitive): ")
            member_password = input("Please enter your passsword for Click and Collect program (case-sensitive): ")
            
            if member_username in member_list:
                if member_password in member_list:
                    print ("Successful login. Welcome to your Click and Collect program.")
                    break
                else:
                    print ("Your username or password is incorrect. Please try again later.")
                    exit()
            else:
                print ("Your username or password is incorrect. Please try again later.")
                exit()
        
        elif login_signup == "B":
            member_username = input("Please enter a new username for Click and Collect program. (case-sensitive): ")
            while True:
                member_password = input("Please enter a new passsword for Click and Collect program. (case-sensitive): ")
                if (any(password.isupper() for password in member_password) and any(password.isdigit() for password in member_password) and len(member_password) >= 7):
                    member_list.append(member_username)
                    member_list.append(member_password)
                    print("Account added, you may sign in now.")
                    break
                else:
                    print("Your password must have at least 1 uppercase, 1 number and have at least 7 characters.")
        
        else:
            print("That is not a valid input. Please enter: | A for Login | B for Signup | :")

def add_items():
    print ("Menu for", day_today + ": ")
    if day_today == "Monday":
        print (foodmenu["Monday"])
    elif day_today == "Tuesday":
        print (foodmenu["Tuesday"])
    elif day_today == "Wednesday":
        print (foodmenu["Wednesday"])
    elif day_today == "Thursday":
        print (foodmenu["Thursday"])
    elif day_today == "Friday":
        print (foodmenu["Friday"])
    else:
        print("Sorry, the canteen is not open today.")
        exit()
        
    print ("==================================")
    while True:
        item_added = input("What item would you like to add to your cart (input 0 to exit back to menu)?: ").title()
        if item_added == "0":
            break
        
        elif item_added == "Fresh Fruits" or item_added == "Noodle Snack" or item_added == "Afghan Cookie":
            cart_items.append(item_added + " | $1")
            cart_prices.append(1)
            print("Item added!")
            print("==============================================")
    
        elif item_added == "Hash Brown" or item_added == "Spaghetti Bun":
            cart_items.append(item_added + " | $1.50")
            cart_prices.append(1.50)
            print("Item added!")
            print("==============================================")
            
        elif item_added == "Potato Chips" or item_added == "Popcorn" or item_added == "Chips" or item_added == "Garlic Bread" or item_added == "Sausage Roll" or item_added == "Water" or item_added == "Juicie" or item_added == "Moosie" or item_added == "Slushy" or item_added == "Calci Yum" or item_added == "Hot Chocolate":
            cart_items.append(item_added + " | $2")
            cart_prices.append(2)
            print("Item added!")
            print("==============================================")
            
        elif item_added == "Pizza Bread" or item_added == "Brownie" or item_added == "Pizza" or item_added == "Hot Dog" or item_added == "Potato Puff" or item_added == "Large Sausage Roll" or item_added == "Quiche" or item_added == "Aloe Vera":
            cart_items.append(item_added + " | $3")
            cart_prices.append(3)
            print("Item added!")
            print("==============================================")
            
        elif item_added == "Steam Bun" or item_added == "Noodle Bowl":
            cart_items.append(item_added + " | $3.50")
            cart_prices.append(3.50)
            print("Item added!")
            print("==============================================")
            
        elif item_added == "Chicken Sandwhich" or item_added == "Chicken Sub" or item_added == "Nachos":
            cart_items.append(item_added + " | $4")
            cart_prices.append(4)
            print("Item added!")
            print("==============================================")
        
        elif item_added == "Pie" or item_added == "Butter Chicken Wrap" or item_added == "Sushi":
            cart_items.append(item_added + " | $4.50")
            cart_prices.append(4.50)
            print("Item added!")
            print("==============================================")        
        
        else:
            print("That's not an item on the menu! Please input an item from the menu.")
            print("==============================================")
            
def view_cart():
    print ("This is your cart: ")
    print("==============================================")
    print (*cart_items, sep = "\n")
    cart_total = sum(cart_prices)
    print("==============================================")
    print ("Total = $", cart_total)
    print("==============================================")    

print ("Welcome to the Click and Collect app for BDSC canteen.")

while True:
    try:
        name = input("Please enter your name: ") .capitalize()
        if not name:  
            raise ValueError
        if name.isdigit():
            raise ValueError
        break    
    except ValueError:
        print("That is not a real name! Try again.")     
        
while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except ValueError:
        print("Please input a number.")

print ("Hello, " + name + "!")
if age < 13 or age > 18:
    print("You must be over 13 and under 18 to be able to open an account.")
    exit()

tutor_class = input("Please enter your tutor class (eg. 12B7, 11E7): ") .upper() .strip()

account_log_reg()

while True:
    mode = int(input("What mode would you like to use: | 1. Add items to cart | 2. View Cart | 3. Checkout | 4. Exit App : "))
    print("==============================================")
    if mode == 1:
        add_items()
        
    elif mode == 2:
        view_cart() 
        
    elif mode == 3:
        print("Order placed! Please pickup your order at interval or lunch at the canteen.")
        print("Your details are: \nName:", name, "\nAge:", age, "\nTutor Class:", tutor_class)
                
    elif mode == 4:
        break
        
    else:
        print ("That is not a valid reponse. Please enter 1, 2 or 3")
            
print("Thank you for using Click and Collect for BDSC Canteen. Bye")