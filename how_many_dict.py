animals = {'B': [15], 'u': [10, 15, 5, 2, 6]}
def how_many(aDict):
    counter = 0
    for lists in aDict.values():
        for element in lists:
            counter +=1
    return counter

print(how_many(animals))
