def mySort(lst, f):
    '''
    Sorting algorithm
    :param lst:
    :param f:
    :return:
    '''
    for i in range(len(lst)):
        for j in  range(len(lst)-i-1):
            if f(lst[j], lst[j+1]) == False:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst