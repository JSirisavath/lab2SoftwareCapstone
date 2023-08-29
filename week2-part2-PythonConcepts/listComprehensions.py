# List comprehensions


class_registered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']


# Make a list of only the ITEC classes
# Destructuring to make a copy to a new array/ list - but for only itec classes
# Put a 'c' or element essentially in the list if that condition is true
only_itec = [c.upper() for c in class_registered if c.startswith('ITEC')]

print(only_itec)


high_temps = [-1, 43, 54, 64, 65, 32, 76, 87, 54, -1, 43, -1]


only_real_measurements = [temp for temp in high_temps if temp != -1]


print(only_real_measurements)  # -1 values or filtered outs


temp_celsius = [(temp_f - 32)*5/9 for temp_f in only_real_measurements]

print(temp_celsius)

# One liner version to format floats
formatted_version_of_celsius = ["%.2f" %
                                tempOfCel for tempOfCel in temp_celsius]

print(formatted_version_of_celsius)


# Another version
for temp in temp_celsius:
    print("%.2f" % temp)  # Format to 2 decimal places


# Average
# total divided by how many celsius
average = sum(temp_celsius) / len(temp_celsius)

print(f'The average temp is {"%.2f" % average} celsius')

# .2f is another way to format decimal places


words = ['hola', 'como', 'estas', 'bien']

# The length of each word in words
length = [len(word) for word in words]

print(length)

# Increase by 1

numbers = [2, 4, 6]

list_of_added_numbers = [number+1 for number in numbers]

print(list_of_added_numbers)  # [3,5,7]


# Greater than 0 filter lists

numbersList = [0, 3, 4, 0, 22, 1]

# To filter, you would need to init number first and after the for loop, then add the condition
newNumberListFiltered = [number for number in numbersList if number != 0]

print(newNumberListFiltered)


# Filter non ITEC classes

list_of_classes = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905', 'itec 1100']

itecStrings = ['ITEC', 'itec']

# Any method inside for condition to filter out specific word
# For any, it would need another iterable of words to find and match that contains those specific words
newListOfClassess = [c for c in list_of_classes if any(
    itec in c for itec in itecStrings)]


print(newListOfClassess)

# Can combine filtering and operations

foods = ['cheese pizza', 'peperoni pizza',
         'ice cream', 'veggie pizza', 'tacos']

# Simple english - upper case food for each food inside foods if food is pizza.
pizzasList = [food.upper() for food in foods if 'pizza' in food]


print(pizzasList)  # [PEPPERONI PIZZA, VEGGIE PIZZA]


# DOUBLE Numbers if the number is not 0

numbersList2 = [0, 10, 4, 0, 32]

# multiple the number by 2 for each number in the numberList 2 if the number does not equal to 0
doubledNumbersList = [number * 2 for number in numbersList2 if number != 0]

print(doubledNumbersList)
