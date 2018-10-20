#!/usr/bin/env python3

usernames = ["jeancul", "electra", "biteaucul", "jonas", "gnu", "admin"]

if usernames :
	for username in usernames:
		if username == "admin" :
			print("Hello " + username.title() + ", would you like to see a status report ?")
		else:
			print("Hello " + username.title() + ", how are you today ?")

else : 
	print('There is no users in your f***ing website')


new_users = ['eddy', 'JONAS', 'gorki', 'vulvizar', 'gnu']

if new_users :
	for user in new_users:
		if user.lower() in usernames :
			print("Sorry, the username " + user.title() + " already exists in our database. Try another username.")

		else:
			print("Welcome " + user.title() + " to our website, enjoy the content")

else:
	print("There are no new users.")