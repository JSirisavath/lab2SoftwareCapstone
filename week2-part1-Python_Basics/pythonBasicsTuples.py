# Tuples

# Similar to an array and has objects nested inside the array
city_state = [
    ('Seattle', "WA"),
    ('Portland', "OR"),
    ('San Francisco', "CA"),
]


print(city_state)


# Getting the first city

first_city_and_state = city_state[0]

print(first_city_and_state)  # ('Seattle', "WA")


# Tuple unpacking - Essentially destructuring a object

# City - Seattle
first_city = first_city_and_state[0]

# State = WA
first_state = first_city_and_state[1]

print(first_city)

print(first_state)

# Another way of unpacking is using both variables associated with the unpacking

city, state = first_city_and_state

print([city, state])


animals = ('lion', 'puma', 'tiger')


lion, puma, tiger = animals

print(tiger)


# tuples in functions

def get_distance():
    miles = 1000
    # Convert to km
    km = miles * 1.6
    return miles, km


distances = get_distance()

print(distances[0])  # First element (1000) miles

miles, km = get_distance()

print(km)
