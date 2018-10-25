prompt = "Hi, welcome to Max Renter,"
prompt += "\n========================="
prompt += "\n\n\tDo you want to rent a car ? \t"

rent_car = input(prompt)

if rent_car == 'yes' or rent_car == 'y':
	car = input("\tWhat sort of car do you want ? \t")
	print('\n\tOk I check if we still have a ' + car + ' in our garage.')

else :
	print('OK, bye then')
