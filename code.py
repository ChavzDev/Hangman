#Imports
import random

#Functions
def difficultyMode():
    try:
        dm = int(input("""
        Select a difficulty mode
        ------------------------
        1 - Easy
        2 - Normal
        3 - Hard
        
        """))
        if dm < 1 or dm > 3:
            dm = -1
            raise ValueError()
        return dm
    except ValueError:
        print('The inputed number must be a number between 1 and 3')

def getWords(dm):
    words = []
    limits = [[0,6], [7, 12], [13, 24]]

    try:
        if dm < 0:
            raise ValueError("Value Error")

        with open("/home/codebars/code/Python/Hangman/files/words.txt", "r", encoding="utf-8" ) as wds:
            for word in wds:
                if len(word) > limits[dm][0] and len(word) < limits[dm][1]:
                    words.append(word.rstrip())
            return words #Returns Words

    except FileNotFoundError:
        print("File not found")
    except ValueError as ve:
        print(ve)

def guess():
    try:
        g = str(input('Input a letter to complete the word: ')).lower()
        if g.isnumeric() or len(g) > 1:
            raise ValueError()
    except ValueError:
        g = "error"
    return g

def displayHangman(a):
    hangman = ['''
   +---+
       |
       |
       |
      ===
    ''', 
    '''
   +---+
   O   |
       |
       |
      ===''',
    '''
   +---+
   O   |
   |   |
       |
      ===''',
    '''
   +---+
   O   |
  /|   |
       |
      ===''',
    '''
   +---+
   O   |
  /|\  |
       |
      ===''',
'''
   +---+
   O   |
  /|\  |
  /    |
      ===
''', 
'''
   +---+
   O   |
  /|\  |
  / \  |
      ===
''']
    hangman.reverse()
    print(hangman[a])


def run():
    dm = difficultyMode() - 1
    words = getWords(dm)
    word = random.choice(words);
    keyWord = ["-" for x in range(0, len(word))]
    string = "".join(keyWord)
    attemps = 6
    won = False

    #Init game   
    displayHangman(attemps) #Display Hangman and word
    print(string)

    #Main Function
    while attemps > 0 and won != True:
        inputed = guess()

        if inputed in word:
            for x in range(0, len(word)):
                if inputed == word[x]:
                    keyWord[x] = inputed 
            string = "".join(keyWord)
        else:
            attemps -= 1
            print("Inputed letter, is not in word")
            print("\n")
        
        #Winner
        if string == word:
            print("Congratulations, you have won")
            won = True 
        elif attemps < 1:
            print("You are hanged")
            print("The word you were looking for is: " + str(word))
    
        displayHangman(attemps)
        print(string)
                        
#Entry Point
if __name__ == "__main__":
    run()
