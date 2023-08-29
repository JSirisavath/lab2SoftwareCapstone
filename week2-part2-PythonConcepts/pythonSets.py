# Sets
# Note: Set items are unchangeable, but you can remove items and add new items.


cats = {'Leopard', 'Tiger', 'Cheetah'}

print(cats)  # Why did the order change?


# looping through each cats and printing them in lower case
for cat in cats:
    print(cat.lower())


# Modifying a set
cats.add('puma')
cats.remove('Cheetah')

print(cats)


# Possible to create a set using a set constructor

this_set = set()

# Adding fruits here

this_set.add('Apple')
this_set.add('Bananas')
this_set.add('Cherry')


print(this_set)

# Also use set to add pre values inside the set constructor

predetermined_set = set(('John', 'Jack', 'Matthew'))

print(predetermined_set)


# No duplicates on sets
predetermined_set.add('John')

print(predetermined_set)  # John will not be added again


for name in predetermined_set:
    print(name)


# Lists

# Removing duplicates

bird_lists = ['robin', 'swan', 'swan', 'robin', 'cardinal', 'robin', 'eagle']


# One way of removing duplicates from a list is by converting the previous list to a set, because we know that set does not allow any duplicates. Once it has been converted to set, convert it back to a list

bird_list_no_duplicates = list(set(bird_lists))


for bird in bird_list_no_duplicates:
    print(bird)  # Expect to print out no duplicates of birds
    # Note: Will lose the order of the birds
