favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, langages in favorite_languages.items():
	print('\n' + name.title() + ' favorite langages are :')
	for langage in langages : 
		print('\t- ' + langage.title())