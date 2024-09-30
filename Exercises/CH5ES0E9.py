#stuff = [1,2,3,4,5,5]

def get_mode(stuff):
    """
    >>> get_mode([1, 1, 3, 4])
    [1]

    >>> get_mode([1,2,3,4])
    []

    >>> get_mode([])
    []

    >>> get_mode([1,1,1,2,2,2,3,3,4])
    [1, 2]

    >>> get_mode(['apple','apple','banana'])
    ['apple']

    >>> get_mode(['apple','apple','banana','banana','pear','pear','pear'])
    ['pear']

    >>> get_mode (['banana','banana','apple','apple'])
    ['banana', 'apple']
    """

    #if the list is empty, return an empty list
    if len(stuff) == 0:
        return []

    index_count_tuples = [] # (index, count) tuples

    for i, j in enumerate(stuff): #enumerate makes it so i provides us with the index, while j provides us with the value of that index
        index_count_tuples.append((i, stuff.count(j)))

    #highest number of repetitions (defining the variable)
    highest_count = 0 
    for placeholder, count in index_count_tuples: #when iterating through a list of tuples with 2 variables, we are accessing the two elements in each tuple (unpacking tuples)
        if count>highest_count:
            highest_count = count

    if highest_count == 1:
        highest_count =0
    

    modes = []

    for i, count in index_count_tuples: #iterating and unpacking tuples again
        if count == highest_count and stuff[i] not in modes: #values that are the same will have different indexes, so we need to make sure those values have not been added
            modes.append(stuff[i])

    return(modes)




if __name__ == '__main__':
    import doctest
    doctest.testmod()