print("     ************* Welcome to iShop calculator *************     ")
basket = []
total_price = []
basket_items = input("How many items are there in your basket today? ")
print("Let's get to counting them ....")
for i in basket_items:
 for y in range(1,int(basket_items)+1):
  if int(basket_items) > 0:
   x = int(i) - (int(i)-y)  
   item = input(f"Please tell me the name of the item number {x} ")
   basket.append(item)
   price = float(input("What is the price of " + item + " ? "))
   total_price.append(price)
see_basket = input("Would you like to see your entire basket items? ").lower()
while see_basket != "yes" and see_basket != "no":
  print("Sorry, invalid input")
  see_basket = input("Would you like to see your entire basket items? ")
if see_basket == "yes":
  print(basket)
else:
  input("Press enter to exit")
see_price = input("Would you like to see how much it'll cost? ").lower()
while see_price != "yes" and see_price != "no":
  print("Sorry, invalid input")
  see_price = input("Would you like to see how much it'll cost? ").lower()
if see_price == "yes":
  print(f"{sum(total_price)} $")
else:
  input("Press enter to exit")
