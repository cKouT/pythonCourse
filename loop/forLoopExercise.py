numbers =[value for value in range(1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = [value for value in range(1,21,2)]
print(odd_numbers)

threes_mumbers = [value for value in range(3,30,3)]
print(threes_mumbers)

cubes = [value**3 for value in range(1,11)]
for cube in cubes:
	print(cube)