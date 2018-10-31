def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name : 
		"""Return a full name, neatly formatted."""
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else : 
		full_name = first_name + ' ' + last_name

	return full_name.title()

active = True
# This is an infinite loop!
while active:
	print("\nPlease tell me your name:")
	f_name = input("First name: ")
	l_name = input("Last name: ")
	m_name = input("Middle name:")

	if m_name :
		formatted_name = get_formatted_name(f_name, l_name, m_name)
		print("\nHello, " + formatted_name + "!")

	else:
		formatted_name = get_formatted_name(f_name, l_name)
		print("\nHello, " + formatted_name + "!")