
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

if size == 'S':
  bill = small_pizza
elif size == 'M':
  bill = medium_pizza
elif size == 'L':
  bill = large_pizza

if add_pepperoni == 'Y':
  bill+= 2
  
if extra_cheese == 'Y':
  bill+=1

print (f"Your final bill is: ${bill}.")



