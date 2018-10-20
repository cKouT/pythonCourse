requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping :
	print('Adding mushrooms to your pizza')
if 'extra cheese' in requested_topping :
	print('Adding extra cheese to your pizza')
if 'pepperoni' in requested_topping :
	print('Adding pepperoni to your pizza')

print('\nFinished making your pizza')


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")

	else:
		print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")

else:
	print("Are you sure you want an empty pizza ?\n")

available_toppings = ['mushrooms', 'olives', 'extra cheese', 'pineapple', 'pepperoni', 'green peppers']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("\tSorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza! ")