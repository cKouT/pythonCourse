numbers = list(range(1,6))
print(numbers)

numbers = list(range(1,55))
print(numbers)

squares = []
for value in range(1,11):
  square = value**2
  squares.append(square)
print(squares)

multiplications = []
for value in range(1,11):
  print(value)
  for valuex in range(1,11):
    multiplication = value * valuex
    print(str(value) + " x " + str(valuex) + " = " + str(multiplication) + ".")
    multiplications.append(multiplication)

print(multiplications)
print(max(multiplications))
print(min(multiplications))
print(sum(multiplications))

squares = [value**2 for value in range(1,11)]
print(squares)