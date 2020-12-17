
personajes = ['Eleven','Hall','Urbus','Catris','Kale']
armas = ['Espada','Hacha']
str_List= " - ".join(personajes)

#MENU PRINCIPAL
def menuPersonajes ():
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
			os.system('clear')
			print("Escribe el numero del personaje a elegir")	

def elegirArmas():
	opc2 = True 
	while opc2 == True:
		try:
			for x in range(1):
				for element in armas:
					print(x+1,"",element)
					x = x+1	
			return	int(input("Elige tu arma\n"))	
			opc2= False
		except ValueError:
			print("Elige el numero de arma que quieres")			

# UTILIDADES
def show_Info (player,arma): 
	print("Personaje: ",player,"\nArma: ",arma)		

#TODOS LOS PERSONAJES

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
class Eleven:

	player_Vida = 100
	player_Armadura = 0
	player_Arma_Damage= "15"

def	eleven_Stats (self,player,arma):
	print("Guerrero: ",player,"\nArma: ",arma,"\nVida= ",player_Vida,"\nArmadura= ",player_Armadura,"\n")
def Ataque():
	player_Arma_Damage = random.randint(12,20)	
"""