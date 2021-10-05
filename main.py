from random import randint

"""
secret-word-game
Player gets 7 incorrect guesses
don't let player guess same char (you already guessed that!)
Input: _ _ _ _ _ _ _
response: _ e _ _ _ _ _ 
Hard code word then...
Create list of random words to select from
directory of words on laptop to be imported?

Show number of strikes.
throw guesses into an input ... list.
check to see if guess is on the list


"""
word_list = ['target', 'prime', 'vermin', 'tenderloin', 'lion', 'giraffe', 'month',
'lamp', 'violet', 'indigo', 'absolute', 'python', 'orange', 'cardstock', 'whiteboard', 
'soda', 'jacket', 'tissue', 'extinction', 'dream', 'freedom', 'suffrage', 'butterfly',
'chair', 'literature', 'container', 'screen', 'phone', 'telephone', 'doorway', 'corsage',
'printer', 'window', 'question', 'battleaxe', 'plant', 'stool', 'dishwasher', 'estimate',
'elitism', 'arcade','beast','wolverine', 'storm', 'cyclops', 'vision', 'visionary', 
'artificial', 'heart', 'broken', 'articulate', 'sandy', 'beach','maximum', 'apricot']
target_word = 'target'
strikes = 0
used_guesses = []

def pick_word():
    global target_word
    i = randint(0, len(word_list))
    target_word = word_list[i]

def displayBlanks(target):
    """
    Takes a word, "target" and returns a string consisting of a
    number of "_ "s equal to its length.   
    """ 
    result = ''
    for char in target:
        result += '_ '
    return result

def checkGuess(char):
    """
    Takes character passed in and checks if a) it has been used already
    b) if it is in the target word
    If b is True, then it replaces a blank in current_guess with each 
    instance of that character.
    Returns None

    Side effects: 
    current_guess altered to show progress
    strikes updated if the character isn't in the target_word
    used_guesses appended with character
    """ 
    global strikes
    if char in used_guesses:
        print("You've guessed that one already!  Try again!")
    else: 
        if char in target_word:
            for index, char1 in enumerate(target_word):
                if  char == target_word[index]:
                    current_guess[index] = char1
            used_guesses.append(char)
        else: 
            print("Sorry!  That's not in the word!")
            strikes += 1
            used_guesses.append(char)
            remaining = 7 - strikes
            print(remaining, " strikes remain!")

pick_word()
current_guess = displayBlanks(target_word).split(' ')
current_guess.pop(-1)
alphabet = 'abcdefghijklmnopqrstuvwxyz'

while strikes < 7:
    print(current_guess)
    guess = input('Enter a letter to guess the word!')
    print('/////////////////////////////////////////////')
    if len(guess) == 1 and guess.lower() in alphabet:
        guess = guess.lower()
        checkGuess(guess)
        print("You've already guessed: ", used_guesses)
        if ''.join(current_guess) == target_word:
            print("Congratulations!  You win!")
            break
        if strikes >= 7:
            print("You ran out of guesses!  You lose!")
            print("The word was ", target_word)
            break
    else:
        print('Please enter a letter!')