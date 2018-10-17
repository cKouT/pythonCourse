my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append("kebab")
my_foods.append("couilles de moutons")
friend_foods.append("frites")
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print('\nThe first three items in the list are : ')
for food in my_foods[:3]:
	print(food)

print('\nThree items in the midle of the list are : ')
for food in my_foods[1:4]:
	print(food)

print('\nThree items in the end of the list are : ')
for food in my_foods[-3:]:
	print(food)