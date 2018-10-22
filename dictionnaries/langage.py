#!/usr/bin/env python3

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print("Sarah's favorite programming langage is " +
	favorite_languages['sarah'].title() +
	".")

for name, langage in favorite_languages.items() :
	print( 
		name.title() + 
		"'s favorite lange is " +
		langage.title() + 
		"."
		)

friends = ['phil', 'sarah']

for name in favorite_languages:
	print(name.title())

	if name in friends:
		print('Hi ' + name.title() + ', I see your favorite langage is ' +
			favorite_languages[name].title() + "!"
			)

if 'erin' not in favorite_languages:
	print('Erin, please take our poll')

for name in sorted(favorite_languages):
	print(name.title() + ', thank you for taking the poll')

print('\nThe following languages have been mentioned:')
for langage in set(sorted(favorite_languages.values())):
	print('\t- ' + langage.title())


make_poll = []
make_poll.append('phil')
make_poll.append('jerry')
make_poll.append('jessica')
make_poll.append('john')
make_poll.append('sarah')
make_poll.append('edward')

print(make_poll)

for name in make_poll:
	if name in favorite_languages:
		print('Hi ' + name.title() + ', thank you for responding the poll.')

	else:
		print('Hi ' + name.title() + ', can you respond the poll please ?')