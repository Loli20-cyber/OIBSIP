import math 

weight=float(input("weight in kilometers"))
height=float(input("height in meters"))

heightcm=height*1000

if isinstance(height, float)==False:
    height=float(input("height in meters:"))

if height<=0:
    height=float(input("height in meters:"))

if isinstance(weight,float)==False:
    weight=float(input("weight in kilometers: "))

if weight<=0:
    weight=float(input("weight in kilometers: "))

bmi=weight/(height)**2
if bmi <18.5 :
    print("Underweight")
elif bmi>24.9:
    print("Overweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal")





