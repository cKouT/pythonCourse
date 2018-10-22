# Store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

# Summarize the order
print("You summarized a " + pizza['crust'] +
	"-crust pizza with these following toppings : ")

for topping in pizza["toppings"]:
	print("\t- " + topping)
