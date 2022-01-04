import random
wrong = 0
hangman = (
    """
 ------
|     |
|
|
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|
|
|
|
|
----------
"""
   ,
"""
 ------
|     |
|     0
|     +
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|    -+
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|    -+-
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-\
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-\
|     |
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-\
|     |
|     |
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-\
|     |
|     |
|    |
|    |
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-\
|     |
|     |
|    | |
|    | |
----------
"""
)
words = ("enigma","pneumonia","keyboard", "burger", "sheesh", "broken", "brazil", "vietnam")
guessword = random.choice(words)
guessword = guessword.upper()
wordlength = len(guessword)
fillword = ""
guesslist = []
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def printfunction(lists,textbetweenlist):
	listnobracket = ""
	for c in lists:
		if len(listnobracket) > 0:
			listnobracket = listnobracket + textbetweenlist + c
		else: 
			listnobracket = listnobracket + c
	return listnobracket 

def currentWord(fillword,guess,guessword):
	fillwords = list(fillword)
	i = 0
	j = 0
	for b in guessword:
		if guess == b:
			fillwords[j] = guess
		j += 1
	i += 1	
	return fillwords

for letter in guessword:
	fillword = '-' * wordlength

while wrong < 11 and fillword != list(guessword):
	guess = input("Enter your guess:")
	guess = guess.upper()
	while guess not in alphabet_list:
		print("Try Again!")
		guess = input("Enter your guess:")
		guess = guess.upper()
	fillword = currentWord(fillword,guess,guessword)
	if guess not in guessword:
		wrong += 1
	if guess not in guesslist:
		guesslist.append(guess)
	listnobracket = printfunction(fillword," ")
	guesslistnobracket = printfunction(guesslist," , ")
	print(hangman[wrong])
	print(f"Your current word is {listnobracket}")
	print(f"Your current guesses are {guesslistnobracket}")

if wrong >= 11:
	print("You lost! Try Again!")
else:
	print("You won!")