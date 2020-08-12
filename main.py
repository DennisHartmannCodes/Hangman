import random

STARTING_LIVES = 6

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
  GuessedLetters = []
  word = randomWord()
  userWord = ""
  gotALetter = False
  CurrentLives = STARTING_LIVES
  for g in range(len(word)):
    userWord = userWord + "_"
  
  while (CurrentLives > 0):
    print("Lives: " + str(CurrentLives))
    #print(word)
    print(userWord)
    print("Guessed letters" + str(GuessedLetters))
    value = (input("Please enter a letter:\n")).lower()

    GuessedLetters.append(value)


    for i in range(len(word)):
      if (word[i] == value[0]):
        userWord = userWord[0:i] + value + userWord[i+1:]
        print("The word was " + word)
        print("Good job! You guessed one of the letters!")
        gotALetter = True
    
    if (gotALetter == False):
      print("You didn't guess the right letter.")
      CurrentLives = CurrentLives - 1
      if (CurrentLives == 0):
        print("Sorry, you lost the game.")
        print("The word was " + word)
        break
    

    noBlanks = True
    for x in range(len(word)):
      if(userWord[x] == "_"):
        noBlanks = False
    
    if (noBlanks):
      print("Congrats! You won the game!")
      break
    
    gotALetter = False



def gameLoop():
  print("Hello, this is a game of Hangman that is text based")

  print("You play by entering single characters and the output tells you if it was correct")

  while(True):
    value1 = (input("Would you like to play? (y/n) \n")).lower()

    if(value1 == "y"):
        print("Awesome, Let's go!")
        PlayGame()
    else:
      print("Ok, Have a great day!")
      break


gameLoop()
