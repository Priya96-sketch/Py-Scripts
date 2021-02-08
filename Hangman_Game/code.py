import random
#Importing all the words for the game from words python file.
from words import word_list

#defining a function , which will return a word for our game.
def get_word():
    word = random.choice(word_list)     # "random.choice()" method returns a list with the randomly selected element from the specified sequence.
    return word.upper()             #upper() is a built-in method used for string handling. It will return all the words/strings in uppercase format.

#This "play" function is for the actual interactive game_play.
def play(word):
    word_completion = "_" * len(word)   #This will contain the same "_(dash)" as tehe random chosen word. It will initially contain only underscores.
    guessed = False  #Initialzed to false
    
    #Creating two lists, where "guessed_letters[] will hold the letters user guessed & "guesses_words" will hold the words user guessed.
    guessed_letters = [] 
    guessed_words=[]
    tries = 6  #Total tries given to the user.
    print("Let's play Hangman!")
    print(display_hangman(tries))    #Print the number of tries available for the user
    print(word_completion)           #Print the underscores for guessing the letter.
    print('\n')
    while not guessed and tries > 0:    # Case -> When we haven't entered any letter(when we haven't guessed anything)
        guess = input("Please guess a letter or word: ").upper()   # Taking input from user for guessing or asking to input letters , which will be taken in UpperCase.
       # If only one letter is guessed & isalpha() method returns True if all the characters are alphabet letters.
        if len(guess) == 1 and guess.isalpha():   
            if guess in guessed_letters:   #If our guess is right
                print("You already guessed the letter", guess)
            elif guess not in word:    #If our guess is wrong or not included in the random word generated, then print this
                print(guess, "is not in the word.")
                tries -= 1    # Reducing our tries by minus 1 for incoreect guessing
                guessed_letters.append(guess)
            else:
                print("Good Job,", guess, "is in the word!")    # Case -> If guess is right.
                guessed_letters.append(guess)    
                word_as_list =list(word_completion)    
                
                #Here guess occurs in a word, if word is correct [ CASE -> RIGHT ]
                indices = [ i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess   #Traversing through the loop to  compare each index alphabet with our guessed alphabets.
                    word_completion = "".join(word_as_list)  #Then joining all the alphabets together
                    if "_" not in word_completion:
                        guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess !=word:
                print(guess, "is not the word.")   #For Incorrect Case
                tries -=1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))   #Always remember indexing is very important in Python.
        print(word_completion)          
        print('\n')
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else: 
        print("Sorry, you ran out of tries. The word was" + word + ". Maybe next time!")
def display_hangman(tries):
    stages = [ #final state: head, torso, both arms, and both legs
                    """
                    --------
                    |       |
                    |       O
                    |      \|/
                    |       |
                    |      / \
                    -
                    """,
                    #head, torso, and both arms
                    """
                    --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
                    


