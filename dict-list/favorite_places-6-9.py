favorite_places = {
	'agathe' : ['espagne', 'japon', 'canada'],
	'mael' : ['costa rica', 'japon'],
	'george' : ['suisse', 'autriche', 'espagne'],
	'john' : ['onduras']
}

for key, values in favorite_places.items():
	if len(values) > 1 :	
		print(key.title() + "'s favorite places are :")
		for value in values:
			print('\t- ' + value)
	else : 
		print(key.title() + "'s favorite place is :")
		for value in values:
			print('\t- ' + value)