for item in range(5, 10, 2):
    print(item)
    
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# Nested Loops
for x in range(4):
    for y in range (3):
        print(f'({x}, {y})')
        

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
    
numbers = [10, 5, 10, 5, 5]
for l_count in numbers:
    output = ''
    for count in range(l_count):
        output += 'l'
    print(output)
    
# Lists

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'
print(names)

# Writing a program, to find the largest number in a list
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# Two dimensional list

matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]
#matrix[0] [1] = 20
#print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)
        

# List methods or List function

numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)
#numbers.insert(5) 
#numbers.sort() 
#numbers.reverse()
print(numbers2)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# Tuples
numbers = (1, 2, 3)
print(numbers[0])

# Unpacking
coordinates = [1, 2, 3]
x, y, z = coordinates
print(y)

# Dictionaries

customer = {
  "name": "John Smith",
  "age": 30,
  "is_verified": True
}
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])
#print(customer.get("birthdate", "Jan 1 1980"))

phone = input("Phone: ")
digits_mapping = {
   "1": "One",
   "2": "Two",
   "3": "Three",
   "4": "Four"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)


# emoji converter
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
    ":)": "smiley",
    ":(": "sad"
    }
    output = ""
    for word in words:
      output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))




        