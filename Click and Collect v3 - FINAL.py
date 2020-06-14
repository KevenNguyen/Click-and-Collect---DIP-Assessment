import datetime

date_today = datetime.datetime.now()
day_today = date_today.strftime("%A")

menu_mon = ["Pizza $5", "Pie $3.50", "Sushi $5", "Aloe Vera $3"]
menu_tue = ["Pizza $5", "Pie $3.50", "Sushi $5", "Sausage Roll $2"]
menu_wed = ["Pizza $5", "Pie $3.50", "Sushi $5", "Noodles $3"]
menu_thu = ["Pizza $5", "Pie $3.50", "Sushi $5", "Butter Chicken Wrap $4.50"]
menu_fri = ["Pizza $5", "Pie $3.50", "Sushi $5", "Juicie $2"]

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
        print (*menu_mon, sep = " | ")
    elif day_today == "Tuesday":
        print (*menu_tue, sep = " | ")
    elif day_today == "Wednesday":
        print (*menu_wed, sep = " | ")
    elif day_today == "Thursday":
        print (*menu_thu, sep = " | ")
    elif day_today == "Friday":
        print (*menu_fri, sep = " | ")
    else:
        print("Sorry, the canteen is not open today.")
        exit()
        
    print ("==================================")
    while True:
        item_added = input("What item would you like to add to your cart (input 0 to exit back to menu)?: ").title()
        if item_added == "0":
            break
        
        elif item_added == "Pizza" or "Sushi":
            cart_items.append(item_added + " | $5")
            cart_prices.append(5)
            print("Item added!")
            print("==============================================")
        
        elif item_added == "Pie":
            cart_items.append(item_added + " | $3.50")
            cart_prices.append(3.50)
            
            print("Item added!")    
            print("==============================================")
            
        elif item_added == "Aloe vera":
            cart_items.append(item_added + " | $3")
            cart_prices.append(3)
            print("Item added!")
            print("==============================================")
            
        elif item_added == "Sausage roll":
            cart_items.append(item_added + " | $2")
            cart_prices.append(2)
            print("Item added!")
            print("==============================================") 
            
        elif item_added == "Noodles":
            cart_items.append(item_added + " | $3")
            cart_prices.append(3)
            print("Item added!")
            print("==============================================")
            
        elif item_added == "Butter Chicken Wrap":
            cart_items.append(item_added + " | $4.50")
            cart_prices.append(4.50)
            print("Item added!")
            print("==============================================")
            
        elif item_added == "Jucie":
            cart_items.append(item_added + " | $2")
            cart_prices.append(2)
            print("Item added!")
            print("==============================================") 
            
        elif item_added == "Sushi":
            cart_items.append(item_added + " | $5")
            cart_prices.append(5)
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

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print ("Hello, " + name + "!")
if age < 13:
    print("You must be over 13 to be able to open an account.")
    exit()

tutor_class = input("Please enter your tutor class (eg. 12B7, 11E7): ")

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
                
    elif mode == 4:
        break
        
    else:
        print ("That is not a valid reponse. Please enter 1, 2 or 3")
            
print("Thank you for using Click and Collect for BDSC Canteen. Bye")