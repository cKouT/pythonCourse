pizzas = ['royal', 'calzone', 'margaritta','4 cheeses']
friends_pizzas = pizzas[:]

pizzas.append('3 cheeses')
friends_pizzas.append('hawayii')

print('\nMy favorite pizzas are :')
for pizza in pizzas:
	print(pizza)

print('\nMy friends favorite pizzas are :')
for pizza in friends_pizzas:
	print(pizza)

