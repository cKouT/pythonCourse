# code : utf8

def describe_city(name, country='united states of america'):
	print("\n" + name.title() + " is in " + country.title() + '.')
	pass

describe_city("los angeles")
describe_city('new york')
describe_city('paris', 'france')