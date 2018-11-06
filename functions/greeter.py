def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name : 
		"""Return a full name, neatly formatted."""
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else : 
		full_name = first_name + ' ' + last_name

	return full_name.title()

# This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == "q":
		break
	l_name = input("Last name: ")
	if l_name == "q":
		break

	m_name = input("Middle name:")	
	if m_name == "q":
			break

	if m_name :
		formatted_name = get_formatted_name(f_name, l_name, m_name)
		print("\nHello, " + formatted_name + "!")

	else:
		formatted_name = get_formatted_name(f_name, l_name)
		print("\nHello, " + formatted_name + "!")
