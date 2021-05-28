
#Funcion para limpiar pantalla de consola
import os
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

#Importando Modulo
import calculo

#Definimos la variable que controla el menu
control = 1

#creamos el while que manejara el menu
while control != 0 :
		#Mostramos el menu en compile
		print("------ Calculadora HiperBasica ------")
		print("--- 1- Suma ")
		print("--- 2- Resta")
		print("--- 3- Multiplicar")
		print("--- 4- Division")
		print("--- 5- Raiz Cuadrada")
		print("--- 6- Modulo ")
		print("--- 7- Potenciia")
		print("--- 8- Factorial")
		print("-------------------------------------")
		print("Si deseas salir digite Cero (0) para salir")
		Calculopedido = int (input("Introduzca el numero de la operación que desea realizar: "))
		print("")

		#If de salida de calculadora
		if Calculopedido == 0:
			control=0
			print("Has salido de la calculadora")
			print("")
		#elif para identificar que calculo se desea realizar
		elif Calculopedido == 1 or Calculopedido ==2 or Calculopedido == 3 or Calculopedido == 4 or Calculopedido == 5 or Calculopedido == 6 or Calculopedido == 7 or Calculopedido==8:
			
			#if para calculo de la suma
			if Calculopedido == 1:
				num1 = int (input("Digite el primer numero que desea sumar: "))
				print("")
				num2 = int(input("Digite el segundo numero a sumar: "))
				print("")
				print("El resultado de la suma es la siguiente: ", calculo.operacion(Calculopedido, num1, num2))
			
			#elif calculo para resta
			elif Calculopedido == 2:
				#Variable controla el while de confirmacion
				continuar = 0
				#While para confirmar el resultado negativo
				while(continuar !=1):
					num1 = int (input("Digite el primer numero que desea restar: "))
					print("")
					num2 = int(input("Digite el segundo numero a restar: "))
					print("")
					#Verificamos si quiere obtener un numero negativo 
					if(num2>num1):
						print("La resta que desea realizar, dará un resultado negativo")
						print("")
						continuar = int(input("Si desea continuar digite 1, si desea modifcar los numeros digite 2: "))
					else:
						continuar = 1
				#Lammamos el modulo
				print("El resultado de la resta es la siguiente: ", calculo.operacion(Calculopedido, num1, num2))


			#elif Caculo de multiplicacion
			elif Calculopedido == 3:
				num1 = int (input("Digite el primer numero que desea multiplicar: "))
				print("")
				num2 = int(input("Digite el segundo numero a multiplicar: "))
				print("")
				#Lammamos el modulo
				print("El resultado de la multiplicacion es la siguiente: ", calculo.operacion(Calculopedido, num1, num2))
			

			#elif Calculo de Division
			elif Calculopedido == 4:
				num1 = int (input("Digite el dividendo: "))
				print("")
				num2 = int(input("Digite el divisor: "))
				print("")
				continuar =0
				#if verificador de divisor diferente de 0
				if num2==0:
					while continuar == 0:
						print("El divisor no puede ser 0 (cero), por favor digite un numero diferente: ")
						num2 = int(input())
						print("")
						if num2 != 0:
							continuar = 1
				#Lammamos el modulo
				print("El resultado de la division es la siguiente: ", calculo.operacion(Calculopedido, num1, num2))


			#elif para la Raiz Cuadrada
			elif Calculopedido == 5:
				num1 = int (input("Digite el numero para conocer su raiz cuadrada: "))
				print("")
				num2 = 0
				#Lammamos el modulo
				print("El resultado de la razi cuadrada es la siguiente: ", calculo.operacion(Calculopedido, num1, num2))
			

			#elif para el Modulo
			elif Calculopedido == 6:
				num1 = int (input("Digite el primer numero: "))
				print("")
				num2 = int(input("Digite que modulo del primer numero desea conocer: "))
				print("")
				#Lammamos el modulo
				print("El resultado del modulo es la siguiente: ", calculo.operacion(Calculopedido, num1, num2))

			#elif para la potencia
			elif Calculopedido == 7:
				num1 = int(input("Digite el primer numero: "))
				print("")
				num2 = int(input("Digite la potencia que desea conocer del anterior numero: "))
				print("")
				print("El resultado de la potencia es la siguiente: ", calculo.operacion(Calculopedido, num1, num2))
			
			#elfif para el Factorial
			elif Calculopedido == 8:
				num1 = int(input("Digite el numero del que desea conocer el factorial: "))
				print("")
				print("El resultado del factorial es la siguiente: ", calculo.factorial(num1))



		#else para evitar el ingreso de numeros o letras invalidos
		if Calculopedido != 1 and Calculopedido !=2 and Calculopedido != 3 and Calculopedido != 4 and Calculopedido != 5 and Calculopedido != 6 and Calculopedido != 7 and Calculopedido !=8:
				print("Digito ingresado es invalido")
				print("")
				print("Digite un numero entero para volver al menu, o digite 0 (cero) para salir: ")
				control = int(input())
		
		#Regreso al menu o salir
		print("")
		print("Digite un numero entero para volver al menu, o digite 0 (cero) para salir: ")
		control = int(input())