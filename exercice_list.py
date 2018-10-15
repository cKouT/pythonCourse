guest_list = []

guest_list.append('Joe Cooker')
guest_list.append('David Bowie')
guest_list.append('Jean DuCul')

print(guest_list)
print(len(guest_list))

print('Hey ' + guest_list[0] + ',\nWould you like to diner at home tonight ? \n')
print('Hey ' + guest_list[1] + ',\nWould you like to diner at home tonight ? \n')
print('Hey ' + guest_list[2] + ',\nWould you like to diner at home tonight ? \n')

guest_present = ['David Bowie']
print(guest_list[0] + " and " + guest_list[1] + "cannot come to my diner. \n")
print(len(guest_list))


guest_present.append("marilyn manson")
guest_present.append("mon cul")
print(len(guest_present))

print('Hey ' + guest_present[0].title() + ',\nWould you like to diner at home tonight ? \n')
print('Hey ' + guest_present[1].title() + ',\nWould you like to diner at home tonight ? \n')
print('Hey ' + guest_present[2].title() + ',\nWould you like to diner at home tonight ? \n')

print('Hey ' + guest_present[0].title() + ', ' + guest_present[1].title() + ', and ' + guest_present[2].title() + ". I've found a bigger table.\n I'm going to invite more people. \n")

guest_present.insert(0, 'jimmy endrix')
guest_present.insert(2, 'salma ayek')
guest_present.append('jim morisson')

print('Hey ' + guest_present[0].title() + ',\nWould you like to diner at home tonight ?')
print('Hey ' + guest_present[1].title() + ',\nWould you like to diner at home tonight ?')
print('Hey ' + guest_present[2].title() + ',\nWould you like to diner at home tonight ?')
print('Hey ' + guest_present[3].title() + ',\nWould you like to diner at home tonight ?')
print('Hey ' + guest_present[4].title() + ',\nWould you like to diner at home tonight ?')
print('Hey ' + guest_present[5].title() + ',\nWould you like to diner at home tonight ?')

guest_removed = guest_present.pop()
message = "Sry " + guest_removed.title() + ", I can't invite you anymore, I only can invite 2 people."
print(message)

guest_removed = guest_present.pop(0)
message = "Sry " + guest_removed.title() + ", I can't invite you anymore, I only can invite 2 people."
print(message)

guest_removed = guest_present.pop(0)
message = "Sry " + guest_removed.title() + ", I can't invite you anymore, I only can invite 2 people."
print(message)

guest_removed = guest_present.pop(1)
message = "Sry " + guest_removed.title() + ", I can't invite you anymore, I only can invite 2 people."
print(message)

message = "So, I'm inviting " + guest_present[0].title() + " and " + guest_present[1].title()
print(message)

guest_present.remove('salma ayek')
guest_present.remove('mon cul')

print(guest_present)

guest_list.pop()
guest_list.pop()
guest_list.pop()
print(guest_list)
