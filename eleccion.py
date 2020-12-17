#MODULOS EXTERNOS IMPORTANTES
from personajes import player
#MODULOS DE PYTHON
import os

personajes = ['Eleven','Hall','Urbus','Catris','Kale']
armas = ['Espada','Hacha']
str_List= " - ".join(personajes)

#Objeto de la clase importada PLAYER
nose = player.Peleador()

#Menu principal con elección de personajes
def menuPersonajes():
	opc = True
	while opc == True:
		try:
			for j in range(1):
				for element in personajes:
					print(j+1," ",element)
					j =j+1	
			return int(input("Elige un guerrero\n---->"))
			opc = False
		except ValueError:
			os.system('cls')
			print("Escribe el numero del personaje a elegir")	

#Menu secundario con eleccion de armas del personaje 
def elegirArmas():
	opc = True 
	while opc == True:
		try:
			for x in range(1):
				for element in armas:
					print(x+1,"",element)
					x = x+1	
			return	int(input("Elige tu arma\n"))	
			opc= False
		except ValueError: #SI DIGITA ALFABETO, ERROR
			print("Elige el numero de arma que quieres")

#FUNCION EN FUNCION DEL MODULO EXTERNO from personajes import player
def armaElegida(arma,jugador):
	nose.set_playerName(jugador)
	nose.set_playerHp(100)
	nose.set_playerAr(0)
	nose.set_playerGun(arma)
	nose.show_info()	

"""
def	eleven_Stats(player,arma):
	player_Vida = 100
	player_Armadura = 0
	player_Arma_Damage= "15"
	#random.randint(10,15)

	print("Guerrero: ",player,"\nArma: ",arma,"\nVida= ",player_Vida,"\nArmadura= ",player_Armadura,"\n")

def	hall_Stats(player,arma):
	player_Vida = 100
	player_Armadura = 0
	player_Arma_Damage= "15"
	#random.randint(10,15)

	print("Guerrero: ",player,"\nArma: ",arma,"\nVida= ",player_Vida,"\nArmadura= ",player_Armadura,"\n")

def	urbus_Stats(player,arma):
	player_Vida = 100
	player_Armadura = 0
	player_Arma_Damage= "15"
	#random.randint(10,15)

	print("Guerrero: ",player,"\nArma: ",arma,"\nVida= ",player_Vida,"\nArmadura= ",player_Armadura,"\n")	

def	catris_Stats(player,arma):
	player_Vida = 100
	player_Armadura = 0
	player_Arma_Damage= "15"
	#random.randint(10,15)

	print("Guerrero: ",player,"\nArma: ",arma,"\nVida= ",player_Vida,"\nArmadura= ",player_Armadura,"\n")		

def	kale_Stats(player,arma):
	player_Vida = 100
	player_Armadura = 0
	player_Arma_Damage= "15"
	#random.randint(10,15)

	print("Guerrero: ",player,"\nArma: ",arma,"\nVida= ",player_Vida,"\nArmadura= ",player_Armadura,"\n")	


"""