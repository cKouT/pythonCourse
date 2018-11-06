# code : utf8
def greeter_users(users):
	"""Print a simple greeting for each users"""
	for user in users :
		print('Greetings ' + user.title() + ' !')

usernames = ['bobby', 'billy', 'willy']
greeter_users(usernames)