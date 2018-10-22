users = {
	'aenstein' : {
		'first' : 'albert',
		'last' : 'enstein',
		'location' : 'pinceton'
	},
	'mcurie' : {
		'first' : 'marie',
		'last' : 'curie',
		'location' : 'paris'
	}
}

for username, infos in users.items():
	print('- ' + username.title() + ' :')
	full_name = infos['first'] + ' ' + infos['last']
	location = infos['location']

	print('\t\t Full name : ' + full_name.title())
	print('\t\t Location : ' + location.title())