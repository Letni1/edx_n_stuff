def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    if exp == 0:
        return 1
    else:
        for i in range(1, exp+1):
            result *= base
        return result
print(iterPower(-2.43,4))