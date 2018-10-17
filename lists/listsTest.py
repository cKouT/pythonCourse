bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[1].title())
print(bicycles[2].lower())
print(bicycles[3].upper())

# Dernier objet de la list
print(bicycles[-1])

# Avant dernier et ainsi de suite -3 -4
print(bicycles[-2])

message = "My first bicycle was a " + bicycles[0].title() + ". And it was a very good one"

print(message)

names = ['agathe', 'chou', 'amor']

print(names[0])
print(names[1])
print(names[2])

message = "Selon mon humeur, j'appelle ma copine : " + names[0] + ", " + names[1] + " ou encore " + names[2]
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Switch an item from a list
motorcycles[0] = 'ducati'
print(motorcycles)

# Add an item in a list
motorcycles.append('honda')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Insert element in a list .insert(index, value)

motorcycles.insert(0, 'ducati')
print(motorcycles)

# Delete element from a list
del motorcycles[0]
print(motorcycles)

# Pop out the last element of a list and work with
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.append('suzuki')

last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + ".")

# Pop out an element with his index
first_owned = motorcycles.pop(0)
print("The 1st motorcycle I bought was a " + first_owned.title() + ".")

print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')

# Save and remove an element to use it
too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# Sort a list alphabetical order "ireversble"
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Reverse order
cars.sort(reverse=True)
print(cars)

# Sort reversible way
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")
print(cars)

# Reverse a list 

cars.reverse()
print(cars)

# Finding length of a list
print(len(cars))
