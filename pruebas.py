import random
class Eleven():

	def __init__(self, player, player_vida , player_Armadura ,arma):
		self.player= player
		self.player_vida = player_vida
		self.player_Armadura = player_Armadura
		self.arma = arma

	def getPlayerName(self):
		return print(self.player)

	def setPlayer_HP(self,player_hp):
		self.player_vida = player_hp

	def getPlayer_HP(self):
		return self.player_vida		

	def Atacar_Amigo(self):
		player_Arma_Damage = random.randint(13,20)
		return player_Arma_Damage

import random			
class Enemy(): 

	def __init__(self, enemy_vida, enemy_Armadura,arma):
		self.enemy_vida = enemy_vida
		self.enemy_Armadura = enemy_Armadura
		self.arma = arma

	def setEnemy_HP(self,enemy_hp):
		self.enemy_vida = enemy_hp

	def getEnemy_HP(self):
		return self.enemy_vida	

	def Atacar_Enemy(self):
		enemy_Arma_Damage= random.randint(10,16)
		return enemy_Arma_Damage

import time


v = Eleven("Eleven",100, 0 ,"Hacha")

h = Enemy(0,0,"Espada")
h.setEnemy_HP(100)

vidaE = h.getEnemy_HP()
vidaP = v.getPlayer_HP()

Player_Attack = v.Atacar_Amigo()
Enemy_Attack = h.Atacar_Enemy()



while vidaP > 0 or vidaE > 0:
	print("---------------------------------------------")
	print("vida del enemigo",vidaE)

	print(Player_Attack)
	if Player_Attack >= 18:
		print("Golpe critico")
	vidaE = vidaE - Player_Attack
	if vidaE < 1:
		print("vida del enemigo 0")
		print("HAZ GANADO EL COMBATE")
		print("VIDA TOTAL DEL JUGADOR ",vidaP)
		break
		#MUESTRA LA VIDA ESTANDO EN COMBATE
	elif vidaP > 1:
		print("vida del enemigo FINAL",vidaE)	



	print("---------------------------------------------")
	time.sleep(0.5)


	print("vida del jugador",vidaP)

	print(Enemy_Attack)
	if Enemy_Attack >= 18:
		print("Golpe critico")
	vidaP = vidaP - Enemy_Attack
	if vidaP < 1:
		print("EL ENEMIGO HA GANADO")
		print("VIDA TOTAL DEL JUGADOR ",vidaP)
		break
	elif vidaP > 1:	
		print("vida del jugador FINAL",vidaP)


	

		











"""

while player_Won == 0 or enemy_Won == 0:

	opc = int(input("1. GANA JUGADOR\n2. GANA ENEMIGO\n"))
	if opc == 1:
		print("Jugador gana")
		player_Won = 1
		break
	elif opc == 2:
		print("Enemigo gana")
		enemy_Won=1
		break
	else:
		print("No se xd")	


	print("Vida del jugador")
	v.getPlayer_HP()
	print("Vida del enemigo")
	h.getEnemy_HP()

while player_Won == 0 and enemy_Won == 0:
#ENEMIGO
alea = random.randint(95,100) VIDA
#ENEMIGO 
while player_Vida > 0 and enemy_vida > 0:
	player_Vida = 100
	print(player_vida)

	def __init__(self, player, player_vida, player_Armadura,arma):
		self.player = player
		self.player_vida = player_vida
		self.player_Armadura = player_Armadura
		self.arma = arma

RANDOM CHOISE
Player_vida = 100
Enemy_vida = 80

while player_vida >0 and enemy_vida >0:
      
     Player_damage = random(radint(10,20))

     enemy_vida = enemy_vida - player_damage

     Enrmy damage = random (radint(10,15))

     player_vida = player_vida - enemy_damage

     If player_damage > 17 :        print ("golpe critico")
     If enemy_damage > 14: 
   print ("golpe critico)




import random

player= "Eleven"
arma = "Hacha"
enemy = "Destrozador"
arma = "Espada"

def	eleven_Stats (player,arma):
	player_Vida = 100
	player_Armadura = 0
	player_Arma_Damage= random.randint(10,15)
	arma = arma

	print("Eleven\nGuerrero: ",player,"\nArma: ",arma,"\nVida= ",player_Vida,"\nArmadura= ",player_Armadura,"\n")

def enemigo (enemy,arma):
	enemy_Vida = random.randint(95,100)
	enemy_Armadura = 0
	enemy_Arma_Damage= random.randint(10,15)

	while player_Vida > 0 and enemy_Vida > 0:
		


eleven_Stats(player,arma)
enemigo(enemy,arma)






----------------------------------------------------------------------------
arma_damage= random.randint(10,15)

print(arma_damage)
if arma_damage >= 14:
	print("GOLPE CRÍTICO")
----------------------------------------------------------------------------


----------------------------------------------------------------------------
armas = ['Espada','Hacha']

def elegirArmas():
	for x in range(1):
		for element in armas:
			print(x+1," ",element)
			x = x+1				
----------------------------------------------------------------------------
personajes = ['Eleven','Hall','Urbus','Catris','Kale']
MOSTRAR LISTA DE PERSONAJES ENUMERADOS
for j in range(1):
	for element in personajes:
		print(j+1," ",element)
		j =j+1
----------------------------------------------------------------------------
	"""
