class Peleador:

	def __init__(self, player_Name = "", player_Hp = 0, player_Ar = 0, player_Gun = ""):
		self.player_Name = player_Name
		self.player_Hp = player_Hp
		self.player_Ar = player_Ar
		self.player_Gun = player_Gun

	def set_playerName(self, name):
		self.player_Name = name

	def get_playerName(self):
		return self.player_Name	

	def set_playerHp(self, health):
		self.player_Hp = health

	def get_playerHp(self):
		return self.player_Hp

	def set_playerAr(self, armour):
		self.player_Ar = armour

	def get_playerAr(self):
		return self.player_Ar

	def set_playerGun(self, gun):
		self.player_Gun = gun

	def get_playerGun(self):
		return self.player_Gun				

	def show_info(self):

		diccionario = {
		'Jugador': self.player_Name,
		'Vida': self.player_Hp,
		'Armadura': self.player_Ar,
		'Arma': self.player_Gun
		}

		for key in diccionario:
			 print (key,':', diccionario[key])

#prueba =  Peleador()

#prueba.show_info()		


