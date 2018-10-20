#!/usr/bin/env python3 

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points.')


alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

alien_0['color'] = 'red'
print(alien_0)
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original")