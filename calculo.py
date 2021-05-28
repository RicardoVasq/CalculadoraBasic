import math

def operacion(operacion, num1, num2):
	if operacion == 1:
		return num1 + num2
	elif operacion == 2:
		return num1 - num2
	elif operacion == 3:
		return num1*num2
	elif operacion == 4:
		return num1 / num2
	elif operacion == 5:
		return math.sqrt(num1)
	elif operacion == 6:
		return num1%num2
	elif operacion == 7:
		return math.pow(num1,num2)

def factorial(num1):
	if num1 == 1:
		return 1
	else:
		num1 = num1 * factorial(num1 -1 )
		return num1
