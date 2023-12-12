# Lets us use the random function
import random

# Makes a random integer between 0-5
num = random.randint(0, 5) 

# Different Arrays representing the food categories, with the food items as its data
appetizers = ["Crab Rangoons","Chips", "Dumplings", "Loaded Fries", "Brioche", "Breadsticks"]
main = ["Burgers", "Pizza", "Tacos", "Hot Dogs", "Fish and Chips", "Fried Chicken"]
desert = ["Ice Cream", "Brownie", "Cannoli", "Pie", "Tiramisu", "Cookies"]


print("Random Food Generator!")

# Gets user input, and puts it in itemNumber
itemNumber = input("1 for Appetizer, 2 for Main Course, 3 for Desert: ")

# if statements compare numbers to the userInput, once it gets to the user input it prints out the item of the category corresponding with the random number of the array
if itemNumber == 1: print(appetizers[num])
  
if itemNumber == "2": print(main[num])

if itemNumber == "3": print(desert[num])

# Tells user to have a great day, then ends the code
print("Have a great day!")
exit()
