import random

# home page(battle, train, upgrade)
# 
# Battle
# 10 levels with final boss being op af
# collect coins based on level
# each level is harder
# 
# Train
# costs money to train(increases base health)
# play a mini game in order to increase health
# 
# Upgrade
# Go to shop and buy cool swords(increases range for attacks)

def linebreak():
	print("-------------------------------------")
class Enemy:
	def __init__(self,health,attack):
		self.health = health
		self.attack = attack
	def attackMove(self,playerhealth):
		self.attackrange = random.randint(self.attack - 3, self.attack + (self.health // 2))
		damageamount = playerhealth
		playerhealth = playerhealth - self.attackrange
		damageamount = damageamount - playerhealth
		if playerhealth < 0:
			playerhealth = 0
		return playerhealth,damageamount

enemy = 1
class Player:
	def __init__(self,health,attack):
		self.health = 10
		self.attack = attack
		self.currentsword = "Wooden sword"
		self.coins = 0
	def attackMove(self,enemyhealth):
		swords = {"Wooden sword":5,"Stone sword":8,"Steel sword":10,"Obsidian sword":20,"Diamond sword":40}
		self.attackrange = random.randint(swords[self.currentsword] - 3, swords[self.currentsword] + (self.health // 2))
		damageamount = enemyhealth
		enemyhealth = enemyhealth - self.attackrange
		damageamount = damageamount - enemyhealth
		if enemyhealth < 0:
			enemyhealth = 0
		return enemyhealth,damageamount
	def training(self):
		print(f'Here are your options:\n\nGym: 10 Coins/+5 Health\nSpar: 30 Coins/+20 Health\n\nYou have {self.coins} coins\n\nYou can go back by typing "BACK"\n\n')
		choices = ["GYM","SPAR","BACK"]
		choice = input("What do you want to do? (Type Gym, Spar, or BACK)\n-")
		choice = choice.upper()
		if choice != "BACK":
			while choice not in choices:
				choice = input("That didn't work, please type exactly as listed\n-")
				choice = choice.upper()
			while choice != "BACK":
				while choice not in choices:
					choice = input("That didn't work, please type exactly as listed\n-")
					choice = choice.upper()
				if choice == "GYM" and self.coins < 10:
					choice = (input('You don\'t have enough coins to go to the gym. Try another one or go back by typing "BACK"\n-'))
					choice = choice.upper()
					while choice not in choices:
						choice = input("That didn't work, please type exactly as listed\n-")
						choice = choice.upper()
				elif choice == "GYM" and self.coins >= 10:
					self.coins = self.coins - 10
					self.health = self.health + 5
					print("You got big boy muscles by going to the gym!")
					print(f'You have {player.health} health and {self.coins} coins remaining\n\n')
					choice = input("What do you want to do? (Type Gym, Spar, or BACK)\n-")
					choice = choice.upper()
					while choice not in choices:
						choice = input("That didn't work, please type exactly as listed\n-")
						choice = choice.upper()
				elif choice == "SPAR" and self.coins < 30:
					choice = (input('You don\'t have enough coins to spar. Try another one or go back by typing "BACK"\n-'))
					choice = choice.upper()
					while choice not in choices:
						choice = input("That didn't work, please type exactly as listed\n-")
						choice = choice.upper()
				elif choice == "SPAR" and self.coins >= 30:
					self.coins = self.coins - 30
					self.health = self.health + 20
					print("You sparred Jake Paul and won!")
					print(f'You have {player.health} health and {self.coins} coins remaining\n\n')
					choice = input("What do you want to do? (Type Gym, Spar, or BACK)\n-")
					choice = choice.upper()
					while choice not in choices:
						choice = input("That didn't work, please type exactly as listed\n-")
						choice = choice.upper()

	def upgrade(self):
		print(f'You have {self.coins} coins')
		swordchoice = input('What sword would you like to buy?\n\nStone Sword: 20 Coins\nSteel Sword: 50 Coins\nObsidian Sword: 100 Coins\nDiamond Sword: 200 Coins\n\nIf you would like to go back, type "BACK" \nOtherwise, type the sword name\n-')
		swordchoice = swordchoice.capitalize()
		if swordchoice != "Back":
			swordcost = {"Stone sword":20,"Steel sword":50,"Obsidian sword":100,"Diamond sword":200}
			wordchoice = ["Stone sword","Steel sword","Obsidian sword","Diamond sword","Back"]
			while swordchoice not in wordchoice:
				swordchoice = input("That didn't work, please type exactly as listed\n-")
				swordchoice = swordchoice.capitalize()
			while swordchoice != "Back":
				while swordchoice not in wordchoice:
						swordchoice = input("That didn't work, please type exactly as listed\n-")
						swordchoice = swordchoice.capitalize()
				if swordchoice != "Back":
					if swordcost[swordchoice] > self.coins:
						swordchoice = (input('This item costs too much. Try another one or go back by typing "BACK"\n-'))
						swordchoice = swordchoice.capitalize()
					else:
						self.currentsword = swordchoice
						self.coins = self.coins - swordcost[swordchoice]
						print()
						print(f'You have bought the {swordchoice}!')
						print(f"You have {self.coins} coins left")
						print()
						linebreak()
						print()
						swordchoice = "Back"

	def earnCoins(self,enemy):
		self.coins = self.coins + (enemy)

player = Player(10,5)
levels = {1:"1",2:"?",3:"?",4:"?",5:"?",6:"?",7:"?",8:"?",9:"?",10:"?"}
def highestlevel():
	keys = levels.keys()
	for key in keys:
		if levels[key] == str(key):
			highestmonster = key
	return highestmonster
def battle():
	enemy1 = Enemy(5,5)
	enemy2 = Enemy(20,10)
	enemy3 = Enemy(40,10)
	enemy4 = Enemy(69,20)
	enemy5 = Enemy(80,20)
	enemy6 = Enemy(100,20)
	enemy7 = Enemy(120,30)
	enemy8 = Enemy(150,30)
	enemy9 = Enemy(180,30)
	enemy10 = Enemy(200,30)
	enemylist = {1:enemy1,2:enemy2,3:enemy3,4:enemy4,5:enemy5,6:enemy6,7:enemy7,8:enemy8,9:enemy9,10:enemy10}
	numbers = ["1","2","3","4","5","6","7","8","9","10"]
	highestmonster = highestlevel()
	playerhealth = player.health
	print("There are 10 monsters that you can kill\n")
	print(f'{levels[1]} {levels[2]} {levels[3]} {levels[4]} {levels[5]} {levels[6]} {levels[7]} {levels[8]} {levels[9]} {levels[10]}\n')
	enemy = input("What monster do you want to fight? (Type the number)")
	while enemy not in numbers:
		enemy = input("That didn't work, please type exactly as listed\n-")
	enemy = int(enemy)
	while enemy > highestmonster:
		enemy = input("You haven't unlocked this monster yet. Try another one.\n-")
		while enemy not in numbers:
			enemy = input("That didn't work, please type exactly as listed\n-")
		enemy = int(enemy)

	print()
	print(f'You are fighting a level {enemy} enemy')
	while playerhealth > 0 and enemylist[enemy].health > 0:
		print(f'You have {playerhealth} health and the enemy has {enemylist[enemy].health} health')
		print()
		command = input(f' Type "HIT" to damage the enemy\n-')
		command = command.upper()
		while command != "HIT":
			command = input(f' Type "HIT" to damage the enemy\n-')
			command = command.upper()
		print()
		enemylist[enemy].health, damageamount = player.attackMove(enemylist[enemy].health)
		print(f'You hit the enemy for {damageamount} damage!')
		print(f'The enemy has {enemylist[enemy].health} health and you have {playerhealth} health')
		
		if playerhealth > 0 and enemylist[enemy].health > 0:
			print()
			print("NEXT TURN")
			linebreak()
			print()
			playerhealth, damageamount = enemylist[enemy].attackMove(playerhealth)
			print(f'The enemy has hit you for {damageamount} damage!')
			print(f'The enemy has {enemylist[enemy].health} health and you have {playerhealth} health')
			print()
	if enemylist[enemy].health == 0:
		print()
		print(f'You killed the enemy')
		print(f'You have earned {enemy*10} coins')
		player.earnCoins(enemy*10)
		if enemy == highestmonster:
			highestmonster += 1
			if highestmonster <= 10:
				print(f'You unlocked a level {highestmonster} enemy to fight')
			levels[highestmonster] = str(highestmonster)
		if highestmonster > 10: 
			print("You beat all the enemies!!!")
		linebreak()
	else:
		print(f'You fainted but a person came and brought you back to the home page')
		print()
		linebreak()
		print()
def homepage():
	option = input('Would you like to battle, train, or upgrade?\n\nType BATTLE, TRAIN, or UPGRADE\n\nYou can type QUIT to end the game\n-')
	option = option.upper()
	options = ["BATTLE","TRAIN","UPGRADE","QUIT"]
	while option not in options:
		option = input("That didn't work, please type exactly as listed\n-")
		option = option.upper()
	while option != "QUIT":
		if option == "BATTLE":
			battle()
		if option == "TRAIN":
			player.training()
		if option == "UPGRADE":
			player.upgrade()
		option = input('Would you like to battle, train, or upgrade?\n\nType BATTLE, TRAIN, or UPGRADE\n\nYou can type QUIT to end the game\n-')
		option = option.upper()
		print()
		while option not in options:
			option = input("That didn't work, please type exactly as listed\n-")
			option = option.upper()
homepage()