#MODULOS DE PYTHON
import os
import random

#Clases externas IMPORTANTES
import eleccion
from personajes import player

#Boolean's de WHILE
loop = True
loop2= True

#Variables especificas
jugador = ""
arma = ""

#Objeto de la clase importada PLAYER
nose = player.Peleador()

#Inicio del programa
while loop == True:
	#Ménu con la eleccion principal de los personajes
	opc = eleccion.menuPersonajes()
	
	if 	 opc == 1:		# ELEVEN
		os.system('cls')
		jugador = "Eleven"
		print("Elegiste a",jugador,"\n")
		
		while loop2 == True: #ELECCION DE ARMA
			opc2 = eleccion.elegirArmas()

			if opc2 == 1: #Espada
				os.system('cls')
				arma= "Espada"
				eleccion.armaElegida(arma,jugador)
				loop2 = False			

			elif opc2 == 2: #Hacha
				os.system('cls')
				arma = "Hacha"
				eleccion.armaElegida(arma,jugador)
				loop2 = False

			else:
				print("Arma no encontrada cole")
		break		# FIN ELECCION DE ARMA 	#ELEVEN #dkasdkas
	
	elif opc == 2: 		# HALL
		os.system('cls')
		jugador = "Hall"
		print("Elegiste a",jugador,"\n")
		
		while loop2 == True: #ELECCION DE ARMA
			opc2 = eleccion.elegirArmas()

			if opc2 == 1: #Espada
				os.system('cls')
				arma= "Espada"
				eleccion.armaElegida(arma,jugador)
				loop2 = False			

			elif opc2 == 2: #Hacha
				os.system('cls')
				arma = "Hacha"
				eleccion.armaElegida(arma,jugador)
				loop2 = False

			else:
				print("Arma no encontrada cole")
		break	#HALL
	
	elif opc == 3:		# URBUS
		os.system('cls')
		jugador = "Urbus"
		print("Elegiste a",jugador,"\n")
		
		while loop2 == True: #ELECCION DE ARMA
			opc2 = eleccion.elegirArmas()

			if opc2 == 1: #Espada
				os.system('cls')
				arma= "Espada"
				eleccion.armaElegida(arma,jugador)
				loop2 = False			

			elif opc2 == 2: #Hacha
				os.system('cls')
				arma = "Hacha"
				eleccion.armaElegida(arma,jugador)
				loop2 = False

			else:
				print("Arma no encontrada cole")
		break	#URBUS
	
	elif opc == 4:		# CATRIS
		os.system('cls')
		jugador = "Catris"
		print("Elegiste a",jugador,"\n")
		
		while loop2 == True: #ELECCION DE ARMA
			opc2 = eleccion.elegirArmas()

			if opc2 == 1: #Espada
				os.system('cls')
				arma= "Espada"
				eleccion.armaElegida(arma,jugador)
				loop2 = False			

			elif opc2 == 2: #Hacha
				os.system('cls')
				arma = "Hacha"
				eleccion.armaElegida(arma,jugador)
				loop2 = False

			else:
				print("Arma no encontrada cole")
		break	#CATRIS
	
	elif opc == 5:		# KALE
		os.system('cls')
		jugador = "Kale"
		print("Elegiste a",jugador,"\n")
		
		while loop2 == True: #ELECCION DE ARMA
			opc2 = eleccion.elegirArmas()

			if opc2 == 1: #Espada
				os.system('cls')
				arma= "Espada"
				eleccion.armaElegida(arma,jugador)
				loop2 = False			

			elif opc2 == 2: #Hacha
				os.system('cls')
				arma = "Hacha"
				eleccion.armaElegida(arma,jugador)
				loop2 = False

			else:
				print("Arma no encontrada cole")
		break 	#KALE

	else: 				# CONDICION	
		os.system('cls')
		print("Personaje no encontrado cole")		
