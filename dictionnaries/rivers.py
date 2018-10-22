rivers = {'nile' : 'egypt', 'euphrat' : 'maroco', 'gange' : 'india', 'ragesh' : 'india'}

for k, v in sorted(rivers.items()):
	print('The ' + k.title() + ' runs through ' + v.title())

for river in rivers:
	print(river.title())

for country in set(sorted(rivers.values())):
	print(country.title())