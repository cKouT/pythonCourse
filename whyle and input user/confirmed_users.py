unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users :
	current_user = unconfirmed_users.pop()
	print('The user ' + current_user.title() + ' have been added to our base')

	confirmed_users.append(current_user)

print("\nThe following users have been confirme :")
for user in confirmed_users : 
	print('\t- ' + user.title())