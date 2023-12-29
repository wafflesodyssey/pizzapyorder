#Pizza order program by python based on three sizes and various prices
#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
#Pepperoni for small pizza (Y or N): +$2
#Pepperoni for medium or large pizza (Y or N): +$3
#Extra cheese for any size pizza (Y or N): +$1
print("Thank you for choosing Python Pizza Deliveries!")
size = input()
add_pepperoni = input()
extra_cheese = input()
bill = 0

if size == "S":
      bill += 15
elif size == "M":
      bill += 20
else:
      bill += 25

if add_pepperoni == "Y": #if Y, need to check size
      if size == "S":
          bill += 2
      else: #all other conditions
          bill += 3

if extra_cheese == "Y":
      bill += 1

print(f"Your final bill is: ${bill}.")
    
  

