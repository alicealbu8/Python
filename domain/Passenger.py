class Passenger():
    '''

    '''
    def __init__(self, first_name, last_name, passport_number):
        '''
        Constructor
        :param first_name: string
        :param last_name: string
        :param passport_number: string
        '''
        self.__first_name  = first_name
        self.__last_name = last_name
        self.__passport_number = passport_number

    def __repr__(self):
        return f"Passenger:{self.__first_name} :{self.__last_name} ,passport_number:{self.__passport_number}"

    def getFirstName(self):
        return self.__first_name

    def setFirstName(self, first_name):
        self.__first_name = first_name

    def getLastName(self):
        return self.__last_name

    def setLastName(self, last_name):
        self.__last_name = last_name

    def getPassport(self):
        return self.__passport_number

    def setPassport(self, passport_number):
        self.__passport_number = passport_number

    def getstr(self, string):
        if string in self.__first_name or string in self.__last_name:
            return 1
        else:
            return 0


