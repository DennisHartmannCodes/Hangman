import random

STARTING_LIVES = 6
GuessedLetters = []

WordList = []
file1 = open(r"Words.txt","r")

for x in file1:
  WordList.append((x.replace("\n", '')[:-1]))


def randomWord():
  while(True):
    word = WordList[random.randrange(0,10000)]
    if(len(word) > 3):
        return word


def PlayGame():
  word = randomWord()
  userWord = ""
  gotALetter = False
  CurrentLives = STARTING_LIVES
  for g in range(len(word)):
    userWord = userWord + "_"
  
  while (CurrentLives > 0):
    print("Lives: " + str(CurrentLives))
    print(word)
    print(userWord)
    value = (input("Please enter a letter:\n")).lower()


    for i in range(len(word)):
      if (word[i] == value[0]):
        userWord = userWord[0:i] + value + userWord[i+1:]
        print("Good job! You guessed one of the letters!")
        gotALetter = True
    
    if (gotALetter == False):
      print("You didn't guess the right letter.")
      CurrentLives = CurrentLives - 1
    
    gotALetter = False


PlayGame()
