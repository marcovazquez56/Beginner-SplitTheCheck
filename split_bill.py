print("Welcome to the tip calculator")
total_bill = int(input("What was the total bill? "))
tip = int(input("What percentage of tip would you like to give? please type 10, 12 or 15: "))/100
people = int(input("How many people will split the bill? "))

total = (total_bill / people) * (1 + tip)
print(total)
