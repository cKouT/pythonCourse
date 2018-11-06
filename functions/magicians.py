def make_great(ungreated, greated):
  while ungreated:
    new_magician = 'great ' + ungreated.pop()
    greated.append(new_magician)

  for name in greated :
    print(name.title())

def show_magicians(names):
  for name in names:
    print(name.title())

great_magicians = []
magicians = ['david copperfield', 'harry potter', 'ron wisley']
show_magicians(magicians)
make_great(magicians[:],great_magicians)