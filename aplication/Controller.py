from Repository.Airport import PlaneRepository
from domain.Passenger import Passenger
class PlaneController():
    '''

    '''
    def __init__(self, plane_repository: PlaneRepository = PlaneRepository()):
        '''
        Constructor of the class. Creating a new controller
        '''
        self.__plane_repository = plane_repository

    def __str__(self) -> str:
        '''
        Returns:
        --------
            str
                string representation of the controller
        '''
        return str(self.__plane_repository)

    def get_planes_c(self):
        '''
        Gets all planes
        :return:
        '''
        return self.__plane_repository.get_planes()

    def add_plane_c(self, number: int, airline_company: str, number_of_seats: int, destination: str, list_passengers: list):
        '''

        Add plane to the repository
        '''
        return self.__plane_repository.add_plane(number, airline_company, number_of_seats, destination, list_passengers)

    def update_by_number_c(self,  number: int,  new_airline_company: str, new_number_of_seats: int, new_destination: str, new_list_passengers: list):
        '''

        Update plane identified by number
        '''
        return self.__plane_repository.update_by_number(number, new_airline_company, new_number_of_seats, new_destination, new_list_passengers)

    def delete_by_number_c(self,  number: int):
        '''

        Delete plane identified by number
        '''
        return self.__plane_repository.delete_by_number(number)

    def sort_by_last_name_c(self, plane_number: int):
        '''

        Sort the passengers in a plane according to their last name
        '''
        return self.__plane_repository.sort_by_last_name(plane_number)

    def sort_by_nr_of_passengers_c(self):
        '''
        Sort the planes according to the number of seats

        '''
        return self.__plane_repository.sort_by_nr_of_passengers()

    def sort_planes_acc_concatenation_c(self):
        '''
        Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
        :return:
        '''
        return self.__plane_repository.sort_planes_acc_to_concatenation()

    def sort_by_substring_c(self, substring: str):
        '''
         Sort planes according to the number of passengers with the first name starting with a given substring
        :return:
        '''
        return self.__plane_repository.sort_by_substring(substring)

    def identify_plane_passport_c(self):
        '''
         Identify  planes  that  have  passengers  with  passport  numbers  starting  with  the  same 3 letters
        :return:
        '''
        return self.__plane_repository.identify_planes_passport()

    def identify_passengers_c(self, plane_number: int, string: str):
        '''
        Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  name contain a string given as parameter
        :return:
        '''
        return self.__plane_repository.identify_passengers(plane_number, string)

    def identify_plane_with_passenger(self, first_name: str, last_name: str):
        '''
        Identify plane/planes where there is a passenger with given name
        '''
        return self.__plane_repository.identify_plane_with_passenger(first_name, last_name)

    def group_Persons_c(self, n: int, plane_number: int):
        '''

        :return:
        '''
        return self.__plane_repository.groupPersons(n, plane_number)

    def construct_solution_c(self, sol, plane_number):
        '''

        :return:
        '''
        return self.__plane_repository.constructSolution(sol, plane_number)

    def group_Planes_c(self, n):
        '''

        :return:
        '''
        return self.__plane_repository.groupPlanes(n)

    def construct_solutionPlanes(self, n):
        '''

        :param n:
        :return:
        '''
        return self.__plane_repository.constructSolutionPlanes(n)




