print ("Welcome to the tip calculator")

bill = float(input("How much is the bill? $ "))
prop = float(input("How much do you want to tip (%) $ ")) / 100
people = int(input("How much people? "))

calc_tip = bill * prop
totl = bill + calc_tip
total = totl / people

print (f"Headcounter: ${total}")