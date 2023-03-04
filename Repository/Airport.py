from domain.Plane import Plane
from utils.sorting import mySort
from utils.search import mySearch
from domain.Passenger import Passenger
from utils.backtracking import initSolution, getLast, getNext, isSolution, isConsistent

class PlaneRepository():
    '''

    '''

    def __init__(self, planes=[]):
        self.__planes = planes.copy()



    def get_planes(self):
        '''
        Get all planes in the airport
        :return:
        '''
        return self.__planes[:]

    def add_plane(self,  number, airline_company, number_of_seats, destination, list_passengers):
        '''
        Add a plane to the airport
        :param number:
        :param airline_company:
        :param destination:
        :param list_passengers:
        :return:
        '''
        for i in range(len(self.__planes)):
            if self.__planes[i].getNumber() == number:
                raise ValueError(f"A plane with the number {number} is already in the airport")

        self.__planes.append(Plane(number, airline_company, number_of_seats, destination, list_passengers))

    def update_by_number(self, number,  new_airline_company, new_number_of_seats, new_destination, new_list_passengers):
        '''
        Update a plane identified by its number
        :param new_airline_company:
        :param new_number_of_seats:
        :param new_destination:
        :param new_list_passengers:
        :return:
        '''
        for i in range(len(self.__planes)):
            if self.__planes[i].getNumber() == number:
                self.__planes[i].setAirline(new_airline_company)
                self.__planes[i].setNumberSeats(new_number_of_seats)
                self.__planes[i].setDestination(new_destination)
                self.__planes[i].setList(new_list_passengers)

    def delete_by_number(self, number):
        '''
        Delete a plane by number
        :param number:
        :return:
        '''
        for i in range(len(self.__planes) - 1, -1, -1):
            if self.__planes[i].getNumber() == number:
                del self.__planes[i]


    def sort_by_last_name(self, plane_number):
        '''
        Sort the passengers in a plane by last name
        :return:
        '''
        for i in range(len(self.__planes)):
            if self.__planes[i].getNumber() == plane_number:
                return mySort(self.__planes[i].getList(), lambda x, y: x.getLastName() < y.getLastName())

        raise ValueError(f"Plane with number {plane_number} does not exist in the airport")

    def sort_by_nr_of_passengers(self):
        '''
        Sort planes according to the number of passengers
        :return:
        '''
        return(mySort(self.__planes, lambda x, y: x.getNumberList() < y.getNumberList()))

    def sort_planes_acc_to_concatenation(self):
        '''
        Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
        :return:
        '''
        return (mySort(self.__planes, lambda x, y: str(x.getNumberList()) + x.getDestination() < str(y.getNumberList()) + y.getDestination()))

    def sort_by_substring(self, substring):
        '''
        Sort planes according to the number of passengers with the first name starting with a given substring
        :param substring:
        :return:
        '''
        return (mySort(self.__planes, lambda x, y: x.getNumberWithSubstring(substring) < y.getNumberWithSubstring(substring)))

    def identify_planes_passport(self):
        '''
        Identify  planes  that  have  passengers  with  passport  numbers  starting  with  the  same 3 letters
        :return:
        '''
        return(mySearch(self.__planes, lambda x: x.getFirst3Letters() == 1))

    def identify_passengers(self, plane_number, string):
        '''
        Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  name contain a string given as parameter
        :return:
        '''
        for i in range(len(self.__planes)):
            if self.__planes[i].getNumber() == plane_number:
                return(mySearch(self.__planes[i].getList(), lambda x: x.getstr(string) == 1))

        raise ValueError(f"Plane with number {plane_number} does not exist in the airport")

    def identify_plane_with_passenger(self, first_name, last_name):
        '''
        Identify plane/planes where there is a passenger with given name
        :param first_name:
        :param last_name:
        :return:
        '''
        return(mySearch(self.__planes, lambda x: x.getFullName(first_name, last_name) == 1))


    def groupPlanes(self, n):
        '''
        Form groups of 𝒌 planes with the same destination but belonging to different  airline companies"
        '''
        list = self.__planes
        domain = [i for i in range(-1, len(list))]
        k = 0
        sol = []
        sol.append(initSolution(domain))
        while (k >= 0):
            isSelected = False
            while ((not isSelected) and (sol[k] < getLast(domain))):
                sol[k] = getNext(sol[k])
                isSelected = isConsistent(sol, f = lambda x, y: list[x].getDestination() != list[y].getDestination()) and isConsistent(sol, f = lambda x, y: list[x].getAirline() == list[y].getAirline())
            if (isSelected):
                if (isSolution(sol, n)):
                    yield sol
                else:
                    k = k + 1
                    sol.append(initSolution(domain))
            else:
                sol.pop()
                k = k - 1
        return sol

    def groupPersons(self, n, plane_number):
        '''
        Form groups of 𝒌 passengers from the same plane but with different last names 𝒌 is a value given by the user
        '''
        list = []
        for i in range(len(self.__planes)):
            if self.__planes[i].getNumber() == plane_number:
                list = self.__planes[i].getList()

        domain = [i for i in range(-1, len(list))]
        k = 0
        sol = []
        sol.append(initSolution(domain))
        while (k >= 0):
            isSelected = False
            while ((not isSelected) and (sol[k] < getLast(domain))):
                sol[k] = getNext(sol[k])
                isSelected = isConsistent(sol, f = lambda x, y: list[x].getFirstName() == list[y].getFirstName())

            if (isSelected):
                if (isSolution(sol, n)):
                    yield sol
                else:
                    k = k + 1
                    sol.append(initSolution(domain))
            else:
                sol.pop()
                k = k - 1
        return sol

    def constructSolution(self, sol, plane_number):
        list = []
        for i in range(len(self.__planes)):
            if self.__planes[i].getNumber() == plane_number:
                list = self.__planes[i].getList()
        ans = []
        for a in sol:
            ans.append(list[a])

        return(ans)

    def constructSolutionPlanes(self, sol):
        ans = []
        for a in sol:
            ans.append(self.__planes[a])

        return(ans)








    



