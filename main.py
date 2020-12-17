import os
import eleccion
import random

loop = True
loop2= True
player = ""
arma = ""

while loop == True:
	opc = eleccion.menuPersonajes()

	# ELEVEN
	if opc == 1:
		os.system('cls')
		print("Elegiste a Eleven")
		player = "Eleven"

		while loop2 == True: #ELECCION DE ARMA

			opc2 = eleccion.elegirArmas()

			if opc2 == 1:
				print("Espada elegida")	
				arma= "Espada"	
				os.system('cls')
				eleccion.eleven_Stats(player,arma)
				loop2 = False			

			elif opc2 == 2:
				print("Hacha elegida")
				arma = "Hacha"
				os.system('cls')
				eleccion.eleven_Stats(player,arma)
				loop2 = False

			else:
				print("Arma no encontrada cole")
		break		# FIN ELECCION DE ARMA 	#ELEVEN #dkasdkas
	# HALL
	elif opc == 2:
		os.system('cls')
		print("Elegiste a Hall")
		player= "Hall"

		while loop2 == True: #ELECCION DE ARMA

			opc2 = eleccion.elegirArmas()

			if opc2 == 1:
				print("Espada elegida")		
				arma= "Espada"	
				os.system('cls')
				eleccion.hall_Stats(player,arma)
				loop2 = False			

			elif opc2 == 2:							
				print("Hacha elegida")
				arma = "Hacha"	
				os.system('cls')
				eleccion.hall_Stats(player,arma)
				loop2 = False

			else:
				print("Arma no encontrada cole")
		break	#HALL
	# URBUS
	elif opc == 3:
		os.system('cls')
		print("Elegiste a Urbus")
		player= "Urbus"

		while loop2 == True: #ELECCION DE ARMA

			opc2 = eleccion.elegirArmas()

			if opc2 == 1:
				print("Espada elegida")	
				arma= "Espada"	
				eleccion.urbus_Stats(player,arma)
				loop2 = False			

			elif opc2 == 2:				
				print("Hacha elegida")
				arma = "Hacha"				
				loop2 = False
				eleccion.urbus_Stats(player,arma)

			else:
				print("Arma no encontrada cole")
		break	#URBUS
	# CATRIS
	elif opc == 4:
		os.system('cls')
		print("Elegiste a Catris")
		player = "Catris"

		while loop2 == True: #ELECCION DE ARMA

			opc2 = eleccion.elegirArmas()

			if opc2 == 1:
				print("Espada elegida")		
				arma= "Espada"	
				eleccion.catris_Stats(player,arma)
				loop2 = False			

			elif opc2 == 2:
				print("Hacha elegida")
				arma = "Hacha"				
				loop2 = False
				eleccion.catris_Stats(player,arma)

			else:
				print("Arma no encontrada cole")
		break	#CATRIS
	#KALE
	elif opc == 5:
		os.system('cls')
		print("Elegiste a Kale")
		player = "Kale"

		while loop2 == True: #ELECCION DE ARMA

			opc2 = eleccion.elegirArmas()

			if opc2 == 1:
				print("Espada elegida")
				arma= "Espada"	
				eleccion.kale_Stats(player,arma)
				loop2 = False			

			elif opc2 == 2:
				print("Hacha elegida")
				arma = "Hacha"				
				loop2 = False
				eleccion.kale_Stats(player,arma)

			else:
				print("Arma no encontrada cole")
		break 	#KALE
		
	else:
		os.system('cls')
		print("Personaje no encontrado cole")		
