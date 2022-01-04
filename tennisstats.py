#create a class for both players on the court
#collect stats for serve %, double faults, scoreline, winners, errors

class Players:

	def __init__(self, name):
		self.name = name
		self.aces = 0
		self.firstservesmade = 0
		self.doublefaults = 0
		self.winners = 0
		self.errors = 0
		self.servetotal = 0
		self.servepercentage = 0
		
	
	def showstats(self):
		print(f"{self.name} has made {self.firstservesmade} first serves")
		print(f"{self.name} has double faulted {self.doublefaults} times")
		print(f"{self.name} has aced {self.aces} times")
		self.servepercentage -= 1
		self.servepercentage += 1.00
		self.servepercentage = self.servepercentage * 100
		self.servepercentage = "{:.2f}".format(self.servepercentage)
		print(f"{self.name}'s first serve percentage is {self.servepercentage}%")
		print(f"{self.name} has {self.winners} winners")
		print(f"{self.name} has {self.errors} errors")

class Scoreline(Players):
	def __init__(self, name):
		Players.__init__(self, name)
		self.gamecount = 0
		self.gamescore = "Love"
		
	
	def showscore(self):
		print(f"The game count is {self.gamecount}")
		print(f"The game score is {self.gamescore}")

p1 = input("Who is the first player of the game?\n-")
p2 = input("Who is the second player of the game?\n-")

scoreline = ["Love","15","30","40","AD","Game"]
player1 = Scoreline(p1)
player2 = Scoreline(p2)
score1 = scoreline.index(player1.gamescore)
score2 = scoreline.index(player2.gamescore)
isplayeroneserve = True
server = ""
yes = ["yes", "yea", "yeah", "ye", "y"]
no = ["no", "nope", "n"]
playerlist = [player1,player2]

def awardpoint(winner, score1, score2):
	if winner == "1":#Add no ad and ad
		if score1 == 3 and score2 != 3 and score2 != 4:
			score1 += 2
		elif score1 == 4:
			score1 += 1
		elif score1 == 3 and score2 == 4:
			score2 -= 1
		elif score1 < 4 and score2 < 4:
			score1 += 1

	if winner == "2":#Add no ad and ad
		if score2 == 3 and score1 != 3 and score1 != 4:
			score2 += 2
		elif score2 == 4:
			score2 += 1
		elif score2 == 3 and score1 == 4:
			score1 -= 1
		elif score2 < 4 and score1 < 4:
			score2 += 1
	return score1,score2

def stattracker():# see who hits a winner/error
	answer = input(f"Who won the point?\n-")
	while answer != "1" and answer != "2":
		print("Try typing 1 or 2")
		answer = input(f"Who won the point?\n-")
	winner = answer
	if winner == "1":
		answer = input(f"Did {player1.name} hit a winner?\n-")
		while answer.lower() not in yes and answer.lower() not in no:
			print("Try typing yes or no")
			answer = input(f"Did {player1.name} hit a winner?\n-")
		if answer in yes:
			player1.winners += 1
		else:
			answer = input(f"Did {player2.name} make an error?\n-")
			while answer.lower() not in yes and answer.lower() not in no:
				print("Try typing yes or no")
				answer = input(f"Did {player2.name} make an error?\n-")
			if answer in yes:
				player2.errors += 1
	else:
		answer = input(f"Did {player2.name} hit a winner?\n-")
		while answer.lower() not in yes and answer.lower() not in no:
			print("Try typing yes or no")
			answer = input(f"Did {player2.name} hit a winner?\n-")
		if answer in yes:
			player2.winners += 1
		else:
			answer = input(f"Did {player1.name} make an error?\n-")
			while answer.lower() not in yes and answer.lower() not in no:
				print("Try typing yes or no")
				answer = input(f"Did {player1.name} make an error?\n-")
			if answer in yes:
				player1.errors += 1
	return winner
while player1.gamecount != 6 and player2.gamecount != 6:# need to add for when 7-5 is possible
	while score1 != 5 and score2 != 5:
		if isplayeroneserve == True:
			server = player1.name
			i = 0

		else:
			server = player2.name
			i = 1

		answer = input(f"Did {server} ace?\n-")
		while answer.lower() not in yes and answer.lower() not in no:
			print("Try typing yes or no")
			answer = input(f"Did {server} ace?\n-")
		if answer in yes:
			playerlist[i].aces += 1
			playerlist[i].firstservesmade += 1
			playerlist[i].servetotal += 1
			playerlist[i].servepercentage = (playerlist[i].firstservesmade)/(playerlist[i].servetotal)
			if isplayeroneserve == True:
				winner = "1"
			else:
				winner = "2"
		else:
			answer = input(f"Did {server} make their first serve?\n-")
			while answer.lower() not in yes and answer.lower() not in no:
				print("Try typing yes or no")
				answer = input(f"Did {server} make their first serve?\n-")
			playerlist[i].servetotal += 1
			if answer in yes:
				playerlist[i].firstservesmade += 1
				playerlist[i].servepercentage = (playerlist[i].firstservesmade)/(playerlist[i].servetotal)
				winner = stattracker()
			else:
				answer = input(f"Did {server} make their second serve?\n-")
				while answer.lower() not in yes and answer.lower() not in no:
					print("Try typing yes or no")
					answer = input(f"Did {server} make their second serve?\n-")
				if answer in no:
					if isplayeroneserve == True:
						winner = "2"
						player1.doublefaults += 1
					else:
						winner = "1"
						player2.doublefaults += 1
				else:
					winner = stattracker()
					

		score1,score2 = awardpoint(winner, score1, score2)


		player1.gamescore = scoreline[score1]
		player2.gamescore = scoreline[score2]
		print()
		print(f"The score is {player1.gamescore}-{player2.gamescore}")
		print()
		if score1 == 5:
			score1,score2 = 0,0
			player1.gamescore = scoreline[score1]
			player2.gamescore = scoreline[score2]
			player1.gamecount += 1
			isplayeroneserve = not isplayeroneserve
			print(f"Game count is {player1.gamecount}-{player2.gamecount}")
			break
		if score2 == 5:
			score1,score2 = 0,0
			player1.gamescore = scoreline[score1]
			player2.gamescore = scoreline[score2]
			player2.gamecount += 1
			isplayeroneserve = not isplayeroneserve
			print(f"Game count is {player1.gamecount}-{player2.gamecount}")
			break
print()
if player1.gamecount == 6:
	print(f"{player1.name} has won the set")
if player2.gamecount == 6:
	print(f"{player2.name} has won the set")
print()
print(f"These are {player1.name}'s stats")
player1.showstats()
print()
print(f"These are {player2.name}'s stats")
player2.showstats()
