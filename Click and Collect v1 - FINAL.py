member_list = ["Keven", "password"]
menu = ["Pizza $5", "Pie $3.50", "Sushi $5"]
cart_prices = []
cart_items = []

print ("Welcome to the Click and Collect app for BDSC canteen.")

name = input("Please enter your name: ")

age = int(input("Please enter your age: "))
tutor_class = input("Please enter your tutor class (eg. 12B7, 11E7): ")

member_username = input("Please enter your username for passsword manager (case-sensitive): ")
member_password = input("Please enter your passsword for password manager (case-sensitive): ")

if member_username and member_password in member_list:
    print("==============================================")
    print ("Successful login. Welcome to your password manager.")
else:
    print ("Your username or password is incorrect. Please try again later")
    exit()

while True:
    mode = int(input("What mode would you like to use: | 1. Add items to cart | 2. View Cart | 3. Checkout | 4. Exit App : "))
    print("==============================================")
    if mode == 1:
        print ("Menu: ")
        print (*menu, sep = " | ")
        print ("==================================")
        while True:
            item_added = input("What item would you like to add to your cart (input 0 to exit back to menu)?: ").capitalize()
            if item_added == "Pizza":
                cart_items.append(item_added + " | $5")
                cart_prices.append(5)
                print("Item added!")
                print("==============================================")
            
            elif item_added == "Pie":
                cart_items.append(item_added + " | $3.50")
                cart_prices.append(3.50)
                
                print("Item added!")    
                print("==============================================")
                
            elif item_added == "Sushi":
                cart_items.append(item_added + " | $5")
                cart_prices.append(5)
                print("Item added!")
                print("==============================================")
                
            elif item_added == "0":
                break
            
            else:
                print("That's not an item on the menu! Please input an item from the menu.")
                print("==============================================")
        
    elif mode == 2:
        print ("This is your cart: ")
        print("==============================================")
        print (*cart_items, sep = "\n")
        cart_total = sum(cart_prices) 
        print("==============================================")
        print ("Total = $", cart_total)
        print("==============================================")
        
    elif mode == 3:
        print("Order placed! Please pickup your order at interval or lunch at the canteen.")
                
    elif mode == 4:
        break
        
    else:
        print ("That is not a valid reponse. Please enter 1, 2 or 3")
            
print("Thank you for using Click and Collect for BDSC Canteen. Bye")