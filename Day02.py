print ("Welcome to the tip calculator")

bill = float(input("How much is the bill? $ "))
prop = (input("How much do you want to tip (%) $ ")) / 100
people = int(input("How much people? "))

calc_tip = bill * prop
total = calc_tip / people

print ("Headcounter: ")
print (total)