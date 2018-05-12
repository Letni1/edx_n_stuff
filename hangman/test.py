import string

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    return set(secretWord).issubset(set(lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = list(secretWord)
    for letter in secretWord:
        if letter not in lettersGuessed:
            secretWord[secretWord.index(letter)] = "_"
    return ' '.join(map(str, secretWord))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    check = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in check:
            check.remove(letter)
    return ''.join(map(str, check))


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game Hangman!'+'\nI am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    print('-----------')
    counter = 8
    lettersGuessed = []

    while counter > 0:
        print('You have ' + str(counter) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()

        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
        elif guess not in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            counter -= 1
            print('-----------')
        elif guess in secretWord and guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
        elif guess not in secretWord and guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print('-----------')

        if isWordGuessed(secretWord, lettersGuessed):
            return 'Congratulations, you won!'

    if counter == 0:
        return 'Sorry, you ran out of guesses. The word was %s.' % secretWord



print(hangman('apple'))


