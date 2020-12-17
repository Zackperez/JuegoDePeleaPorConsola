import os
import eleccion
import random
from personajes import player

loop = True
loop2= True
jugador = ""
arma = ""

def eleccionPersonajeArmas(jugador):
	jugador_elegido = jugador

	print(f"Haz elegido a{jugador_elegido}")

nose = player.Peleador()
while loop == True:
	opc = eleccion.menuPersonajes()

	# ELEVEN
	if opc == 1:

		print("Elegiste a Eleven\n")
		jugador = "Eleven"

		while loop2 == True: #ELECCION DE ARMA

			opc2 = eleccion.elegirArmas()

			if opc2 == 1:
				print("Espada elegida\n")	
				arma= "Espada"
				nose.set_playerName(jugador)
				nose.set_playerHp(100)
				nose.set_playerAr(0)
				nose.set_playerGun(arma)
				nose.show_info()
				loop2 = False			

			elif opc2 == 2:
				print("Hacha elegida\n")
				arma = "Hacha"
				nose.set_playerName(jugador)
				nose.set_playerHp(100)
				nose.set_playerAr(0)
				nose.set_playerGun(arma)
				nose.show_info()
				loop2 = False

			else:
				print("Arma no encontrada cole")
		break		# FIN ELECCION DE ARMA 	#ELEVEN #dkasdkas
	# HALL
	elif opc == 2:
		os.system('cls')
		print("Elegiste a Hall")
		jugador= "Hall"

		while loop2 == True: #ELECCION DE ARMA

			opc2 = eleccion.elegirArmas()

			if opc2 == 1:
				print("Espada elegida")		
				arma= "Espada"	
				os.system('cls')
				eleccion.hall_Stats(jugador,arma)
				loop2 = False			

			elif opc2 == 2:							
				print("Hacha elegida")
				arma = "Hacha"	
				os.system('cls')
				eleccion.hall_Stats(jugador,arma)
				loop2 = False

			else:
				print("Arma no encontrada cole")
		break	#HALL
	# URBUS
	elif opc == 3:
		os.system('cls')
		print("Elegiste a Urbus")
		jugador= "Urbus"

		while loop2 == True: #ELECCION DE ARMA

			opc2 = eleccion.elegirArmas()

			if opc2 == 1:
				print("Espada elegida")	
				arma= "Espada"	
				eleccion.urbus_Stats(jugador,arma)
				loop2 = False			

			elif opc2 == 2:				
				print("Hacha elegida")
				arma = "Hacha"	
				eleccion.urbus_Stats(jugador,arma)		
				loop2 = False
				
			else:
				print("Arma no encontrada cole")
		break	#URBUS
	# CATRIS
	elif opc == 4:
		os.system('cls')
		print("Elegiste a Catris")
		jugador = "Catris"

		while loop2 == True: #ELECCION DE ARMA

			opc2 = eleccion.elegirArmas()

			if opc2 == 1:
				print("Espada elegida")		
				arma= "Espada"	
				eleccion.catris_Stats(jugador,arma)
				loop2 = False			

			elif opc2 == 2:
				print("Hacha elegida")
				arma = "Hacha"				
				loop2 = False
				eleccion.catris_Stats(jugador,arma)

			else:
				print("Arma no encontrada cole")
		break	#CATRIS
	#KALE
	elif opc == 5:
		os.system('cls')
		print("Elegiste a Kale")
		jugador = "Kale"

		while loop2 == True: #ELECCION DE ARMA

			opc2 = eleccion.elegirArmas()

			if opc2 == 1:
				print("Espada elegida")
				arma= "Espada"	
				eleccion.kale_Stats(jugador,arma)
				loop2 = False			

			elif opc2 == 2:
				print("Hacha elegida")
				arma = "Hacha"				
				loop2 = False
				eleccion.kale_Stats(jugador,arma)

			else:
				print("Arma no encontrada cole")
		break 	#KALE
		
	else:
		os.system('cls')
		print("Personaje no encontrado cole")		
