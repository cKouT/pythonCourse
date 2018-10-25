sandwich_orders = ['kebad', 'pastrami', 'pastrami', 'tuna', 'cheese', 'vegan',
	'pastrami',]
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich_order = sandwich_orders.pop()
	print('I made your ' + sandwich_order + ' sandwich')

	finished_sandwiches.append(sandwich_order)

print('\nTheese sandwiches are ready : ')

for finished_sandwiche in finished_sandwiches:
	print('\t- ' + finished_sandwiche)

