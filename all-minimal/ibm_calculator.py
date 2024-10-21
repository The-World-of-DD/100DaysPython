height = float(input("How much is yout height(in meters)? "))
weight = float(input("... and your weight(in kg)? "))

# Calculate the bmi using weight and height.
bmi = weight / (height ** 2);
#el 2f y el f al principio es para enseñar los dos ultimos decimales el {} esta resercado en el print
print(f"Your BMI is: bmi {bmi:2f}")
if bmi < 18.5:
    print ("Underweight");
elif 18.5 <= bmi < 24.9:
    print ("Normal");
else:
    print ("Overweight");

#en base a esos condicionales se pueden enseñar diferentes imagenes o formas de una persona... podemos probar con los asciis
