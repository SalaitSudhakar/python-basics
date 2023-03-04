""" BMI FORMULA
BMI = weight in kg / (height in m power(^) 2)
"""

height = float(input("Enter your height in metre: "))
weight = float(input("Enter your weight in kilogram: "))
bmi = int(weight / (height ** 2))
print("Your BMI is", bmi)

if bmi < 18.5 :
    print("You have underweight.")
elif bmi < 25 :
    print("You have normal weight.")
elif bmi < 30 :
    print("You are slightly overweight.")
elif bmi < 35 :
    print("You have obese.")
else :
    print("You are clinically obese.")
