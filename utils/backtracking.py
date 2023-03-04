def initSolution(domain):
    return domain[0]


def getLast(domain):
    return domain[len(domain) - 1]


def getNext(el):
    return el + 1


def isSolution(sol, groupSize):
    return len(sol) == groupSize


def isConsistent(sol, f):
    for i in range(len(sol) - 1):
        if f(sol[-1], sol[i]):
            return False

    return True