class User():
    # Store the users informations
    def __init__(self, first_name, last_name, location, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.email = email
        self.phone = phone

    def describe_user(self):
        print('Hi ' + self.first_name.title() + ' ' +
              self.last_name.title() + ' : '
              '\n \t - Location : ' + self.location.title() +
              '\n \t - Email : ' + self.email +
              '\n \t - Phone : ' + self.phone
              )

moi = User('maël', 'prost', 'saint-pierre', 'metm@gmail.com', '06.92.92.34.56')
moi.describe_user()