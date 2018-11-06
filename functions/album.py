# coding : utf8
def make_album(autor, name):
	
	album = {'artist' : autor, "name": name}
	return album

while True : 
	print("\n\n***** Here we are makin albums *****")
	print("(enter 'q' at any time to quit)")

	a_autor = input('\nPlease enter an artist name: ')
	if a_autor == 'q':
		break
	a_name = input('Enter one of his album name: ')
	if a_name == 'q':
		break
	album_maked = make_album(a_autor, a_name)

	print(album_maked)