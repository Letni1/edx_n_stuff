def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    guess = len(aStr) // 2
    if len(aStr) == 0:
        return False
    elif char == aStr[guess]:
        return True
    elif char > aStr[guess]:
        return isIn(char, aStr[guess + 1:len(aStr)])
    elif char < aStr[guess]:
        return isIn(char, aStr[0:guess])


print(isIn("d", "abcdefg"))