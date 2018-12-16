class Restaurant():
    # Model a restaurant (name and type)
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print('Hi, welcome to the ' + self.name.title() +
              ', we make ' + self.type.title() + ' food. '
              '\nWould you like to order a table ?\n')

    def open_restaurant(self):
        print('The resaurant is open\n')


city_fock = Restaurant('City Fock', 'Chinese')

print(city_fock.name.title())
print(city_fock.type.title())

city_fock.describe_restaurant()
city_fock.open_restaurant()

grilladin = Restaurant('burger king', 'american')
grilladin.describe_restaurant()

akito = Restaurant('akito', 'japanese')
akito.describe_restaurant()
