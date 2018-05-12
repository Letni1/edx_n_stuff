def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    test = min(a, b)
    while test > 1:
        if a % test == 0 and b % test == 0:
            return test
        else:
            test -= 1


print(gcdIter(9, 12))
