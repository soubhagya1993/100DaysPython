print("Welcome to tip calculator.")
x = float(input("What was the total bill? "))
y = int(input("How many people split? "))
z = int(input("What percentage you want to tip? 10, 12 or 15? "))

tip = (x / y) * (z/100)

print ("Tip per person should give is " + str(tip) )

# print(f"Each person should pay: ${tip}")   # Can also be printed like this