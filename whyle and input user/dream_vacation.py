# Create dict for insert infos
dream_vacations = {}
# Text prompt
prompt = '\nIf you could visit one place in the world, where would you go? \n->'
# Define a flag
active = True

while active:
	# Ask user name
	username = input('\nWhat is your name? \n->')
	# Where is your dream vacation
	vacation_place = input(prompt)
	dream_vacations[username] = vacation_place
	# Continu or not ?

	print('\n' + username.title() + ' would like to go to : ' + vacation_place.title())

	continu = input('\nContinue? y / n : \n->')

	if continu == 'n':
		active = False

# Print list users and answers
for name, place in dream_vacations.items(): 
	print(name.title() + "'s vacation dream is " + place.title())