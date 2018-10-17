poisson = "carangue"

print(poisson == "carangue")
print(poisson != "carangue")

poisson = "Carangue"

print(poisson.lower() == "carangue")
print(poisson.upper() != "carangue")
print(poisson.title() != "Carangue")

total = 21

print("\ntotal :")
print(total == 21 and total < 10)

print("\ntotal :")
print(total == 21 and total > 15)

chien = ["niuk", "bigoudi"]
print("niuk" in chien)

print("niuk" not in chien)