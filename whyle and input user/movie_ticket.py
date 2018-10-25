prompt= 'How old are you ?'
while True : 	
	age= input(prompt)
	age= int(age)

	if age < 3:
		print('You are ' + str(age) + ' years old, ok then, the ticket is free. ')

	elif age < 12:
		print('You are ' + str(age) + ' years old, the ticket cost 10$. ')

	elif age >= 12:
		print('You are ' + str(age) + ' years old, the ticket cost 15$')

	else: 
		break

