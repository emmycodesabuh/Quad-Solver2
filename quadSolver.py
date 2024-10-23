# import all needed math functions
import math as m

def title():
	print("************ Simple Quadratic Solver *************")
	print("*\t\t\t\t\t\t *")
	print("\n*  The Best Tool for Solving Quadratic Equations *")
	print("\n*\t    Developer => EmmycodezStudio         *")
	print("\n*\t        Date => 4/12/23                  *")
	print("\n*\t\t\t\t\t\t *")
	print("\n**************************************************")

def calc():
	print("\nEnter a, b, c: ")
	
	print("\na: ")
	a = int(input())
	
	print("\nb: ")
	b = int(input())
	
	print("\nc: ")
	c = int(input())
	
	#Display Equation
	B, C = "", ""
	
	if b > 0:
		B = "+"
	else:
		B = "-"
	if c > 0:
		C = "+"
	else:
		C = "-"
		
	#print the eqn using the absolute values of variables to eliminate unwanted -ve data forms
	if a == 1:
		#using the format ax²+bx+c = 0
		print(f"x² {B} {int(m.fabs(b))}x {C} {int(m.fabs(c))} = 0")
	elif a > 1:
		print(f"{a}x² {B} {int(m.fabs(b))}x {C} {int(m.fabs(c))} = 0")
	
	# Let D = (b²-4ac)
	# x = (-b ± √b²-4ac)/2a
	D = (m.pow(b, 2) - (4*a*c))
	# if D > 0, roots are real (valid)
	if D > 0:
		x1 = ((-b + m.sqrt(D)) / (2*a))
		x2 = ((-b - m.sqrt(D)) / (2*a))
		
		print(f"\n roots are {int(x1)} or {int(x2)}")
	# if D = 0, roots are real (valid)
	# x = -b/2a
	elif D == 0:
		x = (-b / (2*a))
		print(f"\n root is {int(x)}")
	# if D < 0, roots are unreal (invalid)
	else:
		print("\nInvalid Expression")
		print("\nCannot compute unreal roots")


title()
print("WELCOME!!!")
calc()

while True:
	print("\nCalculate again? Yes/No: ")
	ans = input()
	if ans == "yes" or ans == "ye" or ans == "y":
		calc()
	else:
		print("\nGOODBYE!!!")
		break
	