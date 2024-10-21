print("Welcome to the Tonny Peperonni Pizzas!")
size = input("Size? S, M, L: ")
spice = input("Do you prefer a spicy peperonni? Y/N ")
extra_cheese = input("lastly... extra cheese? Y/N ")
bill = 0

if size == "S" or size == 's':
    bill += 9.95
elif size == "M" or size == 'm':
    bill += 13.95
elif size == "L" or size == 'l':
    bill += 17.95

if spice.lower() == "y":
    bill += 3.05
if extra_cheese.lower() == "y":
    bill += 3.15

print(f"Final bill is: ${bill}")#puedes incluir variables en los prints con el $... Importante poner el tipo de variable para poder acceder a la misma en el print
