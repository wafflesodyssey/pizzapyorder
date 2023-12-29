#Pizza order program by python based on three sizes and various prices
#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
#Pepperoni for small pizza (Y or N): +$2
#Pepperoni for medium or large pizza (Y or N): +$3
#Extra cheese for any size pizza (Y or N): +$1
print("Thank you for choosing Python Pizza Deliveries!")
size = input() #size pizza? S, M, L
add_pepperoni = input() #Y or N
extra_cheese = input() #Y or N
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size")

if add_pepperoni == "Y":
    if size == "S":
      bill += 2
elif size == "M" or size == "L":
    bill += 3

if extra_cheese == "Y":
    bill = bill + 1
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}")
    
  

