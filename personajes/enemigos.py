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


import random
class Peleador():

	def __init__(self, player, player_vida , player_Armadura ,arma):
		self.__player= player
		self.__player_vida = player_vida
		self.__player_Armadura = player_Armadura
		self.__arma = arma	

	def setPlayerName(self):
		self.player = player

	def getPlayerName(self):
		return print(player)

	def setPlayer_HP(self,player_hp):
		self.player_vida = player_hp

	def getPlayer_HP(self):
		return self.player_vida		

	def Atacar_Amigo(self):
		player_Arma_Damage = random.randint(13,20)
		return player_Arma_Damage
	
