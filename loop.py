#####################################################
#                 Problem 01
#####################################################

# user input a number
# multiply the number from 1 up to 10
# output should be:
# 10 x 1 = 10
# 10 x 2 = 20
# 10 x 3 = 30
# -----------
# -----------
# 10 x 10 = 100
number = int(input("Enter a Number Here: "))
count = 1
while count <= 10:
  print(number, "x", count, "=", number * count)
  count += 1

#####################################################
#                 Problem 02
#####################################################
number = int(input("Enter a Number Here: "))
temp = number

while number > 0:
  count = temp
  while count > 0:
    print('*', end='')
    count -= 1
  print()
  number -= 1

#####################################################
#                 Problem 03
#####################################################
# You have a blank list. After input one by one food items are added in the blank list
# Once input completed then print the food list
food_list = []
choice = input("Do you want food ? y / n: ")

while choice == "y":
  food_name = input("Enter your item here: ")
  food_list.append(food_name.title())
  print(food_list)
  choice = input("Want to add more items ? y / n: ")
if food_list:
  print("Your items are", food_list)
else:
  print("You added no items")

# #####################################################
#                 Problem 04
# #####################################################
# enter item and item price
# once shopping completed print a list with item name and total price
shop_list = []
total_price = 0

choice = input("Do you want to start shopping ? y / n: ")

while choice == "y":
  item_name = input("Enter Item Name Here: ")
  shop_list.append(item_name.title())
  item_price = int(input("Enter Item Price Here: "))
  total_price = item_price + total_price
  choice = input("Continue shopping ? y / n: ")
  print("Right now your items are", shop_list, "and price is", total_price)
if shop_list:
  print("Your total items are", shop_list, "and total price is", total_price)
else:
  print("You added no items")


# #####################################################
#                 Problem 05
# #####################################################
items_available = ["Chicken", "Vegetables", "Plain Rice", "Daal", "Vorta", "Firni", "Paan Masala"]
customer_ordered_item = []

choice = input("Do you want food ? y / n: ")

while choice == "y":
  food_name = input("Choose your items: ")
  if food_name in items_available:
    customer_ordered_item.append(food_name)
    print(customer_ordered_item)
    choice = input("Do you want more ? y / n: ")
  else:
    print(food_name, "is not available")
if customer_ordered_item:
  print("Your ordered items are", customer_ordered_item)
else:
  print("You added no items")
