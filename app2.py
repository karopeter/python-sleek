# if statements
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


# Imagine the price of a house is $1m
# if the buyer has good credit
# they need to put down 10%
# otherwise they need to put down 20%
# print the down payment

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

# Logical operator
has_high_income = False
has_good_credit = True
has_criminal_record = True

if has_high_income or has_good_credit:
    print("Eligible for loan")
    
if has_good_credit and not has_criminal_record:
    print("Eligible for subsequent loan")
    
# Comparison Operator
temperature = 35

if temperature != 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
    
name = "John Smith"

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be maximum of 50 characters.")
else:
    print("Name looks good!")
    

# Weight converter
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
    
    