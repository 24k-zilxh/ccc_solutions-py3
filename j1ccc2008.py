w=float(input())
h=float(input())
h=h*h
bmi=(w/h)
if 18.5 <= bmi <= 25.0: print('Normal weight')
elif bmi > 25: print("Overweight")
elif bmi < 18.5: print("Underweight")

# this works. solved on 01/21/2023
