cities = {
	'new york' : {
		'country' : 'united states of america',
		'population' : '12 millions',
		'fact' : '2 towers down'
	},
	'goa' : {
		'country' : 'india',
		'population' : '2 millions',
		'fact' : 'great techno'
	},
	'paris' : {
		'country' : 'france',
		'population' : '6 millions',
		'fact' : 'good bread'
	}
}

for city, infos in sorted(cities.items())	:
	country = infos['country'].title()
	population = infos['population']
	fact = infos['fact']

	print('\n' + city.title() + ' is in ' + country + '.')
	print('Its population is ' + str(population) + ' of people.')
	print('And they have ' + fact + '.')
	