from domain.Passenger import Passenger
class Plane():
    def __init__(self, number, airline_company, number_of_seats, destination, list_passengers):
        '''
        Constructor
        :param number:
        :param airile_company:
        :param destination:
        :param list_passengers:
        '''
        self.__number = number
        self.__airline_company = airline_company
        if number_of_seats < 0:
            raise ValueError("Number of seats should be a positive number!")
        else:
            self.__number_of_seats = number_of_seats
        self.__destination = destination
        self.__list_passengers = list_passengers

    def __repr__(self):
        return f"Plane:{self.__number}, airline_company:{self.__airline_company} , number of seats: {self.__number_of_seats} destination:{self.__destination} ,list_passengers:{self.__list_passengers}  \n"

    def getNumber(self):
        return self.__number

    def setNumber(self, number):
        self.__number = number

    def getAirline(self):
        return self.__airline_company

    def setAirline(self, airline_company):
        self.__airline_company = airline_company

    def getNumberSeats(self):
        return self.__number_of_seats

    def setNumberSeats(self, number_of_seats):
        if number_of_seats < 0:
            raise ValueError("Number of seats should be a positive number!")
        else:
            self.__number_of_seats = number_of_seats

    def getDestination(self):
        return self.__destination

    def setDestination(self, destination):
        self.__destination = destination

    def getList(self):
        return self.__list_passengers

    def add_passenger(self, first_name, last_name, passport_number):
        '''
        Add new passenger
        :param first_name:
        :param last_name:
        :param passport_number:
        :return:
        '''
        for i in range(len(self.__list_passengers)):
            if self.__list_passengers[i].getPassport() == passport_number:
                raise ValueError(f"A person with the passport_number {passport_number} is already in the plane")

        self.__list_passengers.append(Passenger(first_name, last_name, passport_number))

    def get_passengers(self):
        '''
        Get all passengers
        :return:
        '''
        return self.__list_passengers[:]

    def update_by_passport(self, passport, new_first_name, new_last_name):
        '''
        Update person identified by passport
        :param passport:
        :param new_first_name:
        :param new_last_name:
        :return:
        '''
        for i in range(len(self.__list_passengers)):
            if self.__list_passengers[i].getPassport() == passport:
                self.__list_passengers[i].setFirstName(new_first_name)
                self.__list_passengers[i].setLastName(new_last_name)

    def delete_by_passport(self, passport):
        '''
        Delete person identified by passport
        :param passport:
        :return:
        '''
        for i in range(len(self.__list_passengers) - 1, -1, -1):
            if self.__list_passengers[i].getPassport() == passport:
                del self.__list_passengers[i]

    def getNumberList(self):
        nr = 0
        for i in self.__list_passengers:
            nr += 1
        return nr

    def setList(self, list_passengers):
        self.__list_passengers = list_passengers

    def getNumberWithSubstring(self, substring):
        '''
        Calculates how many passengers have a given substring in their last name
        :param substring:
        :return:
        '''
        nr = 0
        for i in range(len(self.__list_passengers)):
            if substring in self.__list_passengers[i].getLastName():
                nr += 1
        return nr

    def getFirst3Letters(self):
        '''
        Checks if the first three letters of the passenger's names are equal
        :return:
        '''
        ok = 1
        for i in range(len(self.__list_passengers)-1):
            for j in range(i+1, len(self.__list_passengers)):
                if self.__list_passengers[i].getPassport()[:3] != self.__list_passengers[j].getPassport()[:3]:
                    ok = 0
        return ok

    def getFullName(self, first_name, last_name):
        '''
        Verify if the first name and last name of a person in the list coincide with a given first name and last name
        :param first_name:
        :param last_name:
        :return:
        '''
        ok = 0
        for i in range(len(self.__list_passengers)):
            if self.__list_passengers[i].getLastName() == last_name and self.__list_passengers[i].getLastName() == first_name:
                ok = 1
        return ok

