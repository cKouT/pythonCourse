prompt = '\n\nHello please enter your toppings : \n'
toppings = []

while True :
	topping = input(prompt)
	toppings.append(topping)

	if topping == 'quit' :
		break

	else : 
		print('You add ' + topping + ' to your toppings.\n')
		print('This is your entire liste : ')

	for topping in toppings : 
		print('\t- ' + topping)