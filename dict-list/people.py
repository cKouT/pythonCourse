#!/usr/bin/env python3
people = []
gordon = {
	'first_name': 'gordon',
	'last_name': 'mayer',
	'age': '64',
	'city': 'salt lake city',
 	}

john = {
	'first_name': 'john',
	'last_name': 'ricci',
	'age': '42',
	'city': 'new york city'
}

monica = {
	'first_name': 'monica',
	'last_name': 'galager',
	'age': '29',
	'city': 'ontario'
}

people.append(john)
people.append(monica)
people.append(gordon)
print(people)

for person in people:
	full_name = person['first_name'] + ' ' + person['last_name']
	age = person['age']
	city = person['city']

	print('\n' + full_name.title() + " : ")
	print('\t- Age ->' + age )		
	print('\t- City ->' + city )		