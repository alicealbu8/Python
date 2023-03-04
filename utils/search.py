def mySearch(lst, f):
    '''
    Determine all elements from the list that satisfy the given criteria f.
    '''
    result = []
    for i in range(len(lst)):
        if f(lst[i]):
            result.append(lst[i])
    return result