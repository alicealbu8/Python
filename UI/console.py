from aplication.Controller import PlaneController
from domain.Plane import Plane
from domain.Passenger import Passenger
from Repository.Airport import PlaneRepository
def print_menu():
    '''
    Print all the commands available
    :return:
    '''
    print("0 - exit program")
    print("1 - Add passenger to a plane")
    print("2 - Delete passenger by passport")
    print("3 - Update passenger by passport")
    print("4 - Get all passengers")
    print("5 - Add plane to the list")
    print("6 - Update plane from the list")
    print("7 - Delete plane from the list")
    print("8 - Sort the passengers in a plane by last name")
    print("9 - Sort planes according to the number of passengers")
    print("10 - Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination")
    print("11 - Sort planes according to the number of passengers with the first name starting with a given substring")
    print("12 - Identify  planes  that  have  passengers  with  passport  numbers  starting  with  the  same 3 letters")
    print("13 - Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  name contain a string given as parameter")
    print("14 - Identify plane/planes where there is a passenger with given name")
    print("15 - Form groups of 𝒌 passengers from the same plane but with different last names 𝒌 is a value given by the user)")
    print("14 -  Form groups of 𝒌 planes with the same destination but belonging to different  airline companies")



def start():
    '''
    Start the user interface
    :return:
    '''
    plane_repo = PlaneController(PlaneRepository([
        Plane(1, "Airline1", 180, "Rome",[Passenger("b", "d", "NC12456"), Passenger("a", "b", "AL12390"), Passenger("a", "c", "OK90897")]),
        Plane(2, "Airline2", 80, "Paris", [Passenger("b", "a", "LJ12456"), Passenger("b", "b", "GH12390")]),
        Plane(3, "Airline3", 200, "Rome",[Passenger("c", "c", "ER12456"), Passenger("c", "b", "PY12390"), Passenger("c", "a", "TR5690")]),
        Plane(4, "Airline4", 100, "Vienna",[Passenger("d", "a", "WQ12456"), Passenger("d", "b", "TK12390"), Passenger("d", "c", "QS8790")])
    ]))
    print_menu()
    command = int(input("Your command is >>> "))
    while command != 0:
        if command == 1:
            try:
                plane = int(input("The number of the plane you want to add the passenger to is... "))
                first_name = input("Passenger' s first name is ")
                last_name = input("Passenger' s last name is ")
                passport = input("Passenger' s passport is ")
                for i in range(len(plane_repo.get_planes_c())):
                    if plane_repo.get_planes_c()[i].getNumber() == plane:
                        plane_repo.get_planes_c()[i].add_passenger(first_name, last_name, passport)
                print(plane_repo.get_planes_c())
            except ValueError as ve:
                print(ve)
        elif command == 2:
            try:
                passport = input("Passport is ")
                for i in range(len(plane_repo.get_planes_c())):
                    plane_repo.get_planes_c()[i].delete_by_passport(passport)
                print(plane_repo.get_planes_c())
            except ValueError as ve:
                print(ve)
        elif command == 3:
            try:
                passport = input("Passport is ")
                new_fistName = input("New first name is ")
                new_lastName = input("New last name is ")
                for i in range(len(plane_repo.get_planes_c())):
                    plane_repo.get_planes_c()[i].update_by_passport(passport, new_fistName, new_lastName)
                print(plane_repo.get_planes_c())
            except ValueError as ve:
                print(ve)
        elif command == 5:
            try:
                number = int(input("Number is "))
                airline = input("Airline is ")
                number_seats = int(input("Number of seats is "))
                destination = input("Destination is ")
                nr_passengers = int(input("How many passengers? "))
                list = []
                for i in range(nr_passengers):
                    passport = input("Passport is ")
                    first_name = input("First name is ")
                    last_name = input("Last name is ")
                    list.append(Passenger(first_name, last_name, passport))
                plane_repo.add_plane_c(number, airline, number_seats, destination, list)
                print(plane_repo.get_planes_c())
            except ValueError as ve:
                print(ve)

        elif command == 6:
            try:
                number = int(input("Number is "))
                new_airline = input("Airline is ")
                new_number_seats = int(input("Number of seats is "))
                new_destination = input("Destination is ")
                nr_passengers = int(input("How many passengers? "))
                list = []
                for i in range(nr_passengers):
                    passport = input("Passport is ")
                    first_name = input("First name is ")
                    last_name = input("Last name is ")
                    list.append(Passenger(first_name, last_name, passport))
                plane_repo.update_by_number_c(number, new_airline, new_number_seats, new_destination, list)
                print(plane_repo.get_planes_c())
            except ValueError as ve:
                print(ve)
        elif command == 7:
            try:
                number = int(input("Number is "))
                plane_repo.delete_by_number_c(number)
                print(plane_repo.get_planes_c())
            except ValueError as ve:
                print(ve)
        elif command == 8:
            try:
                try:
                    plane_number = int(input("Plane number is "))
                    print(plane_repo.sort_by_last_name_c(plane_number))
                except IndexError as ve:
                    print(ve)
            except ValueError as ve:
                print(ve)
        elif command == 9:
            print(plane_repo.sort_by_nr_of_passengers_c())
        elif command == 10:
            print(plane_repo.sort_planes_acc_concatenation_c())
        elif command == 11:
            try:
                substring = input("Substring is ")
                print(plane_repo.sort_by_substring_c(substring))
            except ValueError as ve:
                print("substring should be of type string!!")
        elif command == 12:
            print(plane_repo.identify_plane_passport_c())
        elif command == 13:
            try:
                plane_number = int(input("Plane number is "))
                string = input("String is ")
                print(plane_repo.identify_passengers_c(plane_number, string))
            except ValueError as ve:
                print("Plane number should be an int!!")
        elif command == 14:
            first_name = input("First name is ")
            last_name = input("Last name is ")
            print(plane_repo.identify_plane_with_passenger(first_name, last_name))
        elif command == 15:
            try:
                k = int(input("K is "))
                plane_number = int(input("Plane number is "))
                for s in plane_repo.group_Persons_c(k, plane_number):
                    print(plane_repo.construct_solution_c(s, plane_number))
            except ValueError as ve:
                print("K should be of type int!!")
        elif command == 16:
            try:
                k = int(input("K is "))
                for s in plane_repo.group_Planes_c(k):
                    print(plane_repo.construct_solutionPlanes(s))
            except ValueError as ve:
                print("K should be of type int!!")
        command = int(input("Your command is: "))
    print("Bye...\n")

start()



