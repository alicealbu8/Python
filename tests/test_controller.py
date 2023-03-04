from aplication.Controller import PlaneController
from unittest import TestCase
from domain.Passenger import Passenger
from domain.Plane import Plane
from Repository.Airport import PlaneRepository
class TestController(TestCase):
    '''

    '''

    def setUp(self):
        self.plane_repo = PlaneController(PlaneRepository([
            Plane(1, "Airline1", 180, "Rome",
                  [Passenger("a", "a", "NC12456"), Passenger("a", "b", "AL12390"), Passenger("a", "c", "OK90897")]),
            Plane(2, "Airline2", 80, "Paris", [Passenger("b", "a", "LJ12456"), Passenger("b", "b", "GH12390")]),
            Plane(3, "Airline3", 200, "Budapest",
                  [Passenger("c", "c", "ER12456"), Passenger("c", "b", "PY12390"), Passenger("c", "a", "TR5690")]),
            Plane(4, "Airline4", 100, "Vienna",
                  [Passenger("d", "a", "WQ12456"), Passenger("d", "b", "TK12390"), Passenger("d", "c", "QS8790")])
        ]))


    def test_add_plane(self):
        '''

        :return:
        '''
        self.plane_repo.add_plane_c(5, "Airline5", 150, "Prague",
                                  [Passenger("e", "a", "AD12456"), Passenger("e", "b", "AF12390"),
                                   Passenger("e", "c", "QA8790")])
        list_planes = self.plane_repo.get_planes_c()

        self.assertEqual(list_planes[0].getNumber(), 1)
        self.assertEqual(list_planes[0].getAirline(), "Airline1")
        self.assertEqual(list_planes[0].getNumberSeats(), 180)
        self.assertEqual(list_planes[0].getDestination(), "Rome")
        list = list_planes[0].getList()
        self.assertEqual(list[0].getFirstName(), "a")
        self.assertEqual(list[0].getLastName(), "a")
        self.assertEqual(list[0].getPassport(), "NC12456")

    def test_update_by_number(self):
        '''
        Test function for update by number
        :return:
        '''
        self.plane_repo.update_by_number_c(1, "AirlineA", 300, "Bucharest",
                                         [Passenger("e", "a", "AD12456"), Passenger("e", "b", "AF12390"),
                                          Passenger("e", "c", "QA8790")])
        list_planes = self.plane_repo.get_planes_c()

        self.assertEqual(list_planes[0].getNumber(), 1)
        self.assertEqual(list_planes[0].getAirline(), "AirlineA")
        self.assertEqual(list_planes[0].getNumberSeats(), 300)
        self.assertEqual(list_planes[0].getDestination(), "Bucharest")
        list = list_planes[0].getList()
        self.assertEqual(list[0].getFirstName(), "e")
        self.assertEqual(list[0].getLastName(), "a")
        self.assertEqual(list[0].getPassport(), "AD12456")

        # chech if the other planes are unchanged

        self.assertEqual(list_planes[1].getNumber(), 2)
        self.assertEqual(list_planes[1].getAirline(), "Airline2")
        self.assertEqual(list_planes[1].getNumberSeats(), 80)
        self.assertEqual(list_planes[1].getDestination(), "Paris")
        list = list_planes[1].getList()
        self.assertEqual(list[0].getFirstName(), "b")
        self.assertEqual(list[0].getLastName(), "a")
        self.assertEqual(list[0].getPassport(), "LJ12456")

    def test_delete_by_number(self):
        '''
        Test function for delete by number
        :return:
        '''
        self.plane_repo.delete_by_number_c(1)
        list_planes = self.plane_repo.get_planes_c()
        self.assertEqual(list_planes[0].getNumber(), 2)
        self.assertEqual(list_planes[0].getAirline(), "Airline2")
        self.assertEqual(list_planes[0].getNumberSeats(), 80)
        self.assertEqual(list_planes[0].getDestination(), "Paris")
        list = list_planes[1].getList()
        self.assertEqual(list[0].getFirstName(), "c")
        self.assertEqual(list[0].getLastName(), "c")
        self.assertEqual(list[0].getPassport(), "ER12456")

    def test_sort_by_last_name(self):
        '''
        Test function for sort by last name
        :return:
        '''
        self.plane_repo.sort_by_last_name_c(1)
        list_planes = self.plane_repo.get_planes_c()
        list_passengers = list_planes[0].getList()
        self.assertEqual(list_passengers[0].getFirstName(), "a")
        self.assertEqual(list_passengers[0].getLastName(), "a")
        self.assertEqual(list_passengers[0].getPassport(), "NC12456")

        self.plane_repo.sort_by_last_name_c(3)
        list_passengers = list_planes[2].getList()
        self.assertEqual(list_passengers[0].getFirstName(), "c")
        self.assertEqual(list_passengers[0].getLastName(), "a")
        self.assertEqual(list_passengers[0].getPassport(), "TR5690")

        self.assertEqual(list_passengers[1].getFirstName(), "c")
        self.assertEqual(list_passengers[1].getLastName(), "b")
        self.assertEqual(list_passengers[1].getPassport(), "PY12390")

    def test_sort_by_number_of_passengers(self):
        '''
        Test function for sort by number of passengers
        :return:
        '''
        self.plane_repo.sort_by_nr_of_passengers_c()
        list_planes = self.plane_repo.get_planes_c()

        self.assertEqual(list_planes[0].getNumber(), 2)
        self.assertEqual(list_planes[0].getAirline(), "Airline2")
        self.assertEqual(list_planes[0].getNumberSeats(), 80)
        self.assertEqual(list_planes[0].getDestination(), "Paris")

        self.assertEqual(list_planes[1].getNumber(), 4)
        self.assertEqual(list_planes[1].getAirline(), "Airline4")
        self.assertEqual(list_planes[1].getNumberSeats(), 100)
        self.assertEqual(list_planes[1].getDestination(), "Vienna")

        self.assertEqual(list_planes[2].getNumber(), 3)
        self.assertEqual(list_planes[2].getAirline(), "Airline3")
        self.assertEqual(list_planes[2].getNumberSeats(), 200)
        self.assertEqual(list_planes[2].getDestination(), "Budapest")

    def test_sort_planes_acc_to_concatenation(self):
        '''
        Test function for sort planes according to concatenation
        :return:
        '''
        self.plane_repo.sort_planes_acc_concatenation_c()
        list_planes = self.plane_repo.get_planes_c()

        self.assertEqual(list_planes[0].getNumber(), 2)
        self.assertEqual(list_planes[0].getAirline(), "Airline2")
        self.assertEqual(list_planes[0].getNumberSeats(), 80)
        self.assertEqual(list_planes[0].getDestination(), "Paris")
        list = list_planes[0].getList()
        self.assertEqual(list[0].getFirstName(), "b")
        self.assertEqual(list[0].getLastName(), "a")
        self.assertEqual(list[0].getPassport(), "LJ12456")

        self.assertEqual(list_planes[1].getNumber(), 3)
        self.assertEqual(list_planes[1].getAirline(), "Airline3")
        self.assertEqual(list_planes[1].getNumberSeats(), 200)
        self.assertEqual(list_planes[1].getDestination(), "Budapest")
        list = list_planes[1].getList()
        self.assertEqual(list[0].getFirstName(), "c")
        self.assertEqual(list[0].getLastName(), "c")
        self.assertEqual(list[0].getPassport(), "ER12456")

    def test_sort_by_substring(self):
        '''

        :return:
        '''
        self.plane_repo = PlaneRepository([
            Plane(1, "Airline1", 180, "Rome", [Passenger("aaa", "a", "NC12456"), Passenger("aa", "b", "AL12390"),
                                               Passenger("abc", "c", "OK90897")]),
            Plane(2, "Airline2", 80, "Paris", [Passenger("aab", "a", "LJ12456"), Passenger("b", "b", "GH12390")]),
            Plane(3, "Airline3", 200, "Budapest",
                  [Passenger("c", "c", "ER12456"), Passenger("c", "b", "PY12390"), Passenger("c", "a", "TR5690")]),
            Plane(4, "Airline4", 100, "Vienna",
                  [Passenger("d", "a", "WQ12456"), Passenger("d", "b", "TK12390"), Passenger("d", "c", "QS8790")])
        ])
        self.plane_repo.sort_by_substring("aa")
        list_planes = self.plane_repo.get_planes()

        self.assertEqual(list_planes[0].getNumber(),
                         4)  # we can check only the number of the plane because it is unique
        self.assertEqual(list_planes[1].getNumber(), 3)
        self.assertEqual(list_planes[2].getNumber(), 2)
        self.assertEqual(list_planes[3].getNumber(), 1)

    def test_identify_planes_passport(self):
        '''

        :return:
        '''
        self.plane_repo = PlaneRepository([
            Plane(1, "Airline1", 180, "Rome",
                  [Passenger("a", "a", "NC12456"), Passenger("a", "b", "NC12390"), Passenger("a", "c", "NC10897")]),
            Plane(2, "Airline2", 80, "Paris", [Passenger("b", "a", "LJ12456"), Passenger("b", "b", "GH12390")]),
            Plane(3, "Airline3", 200, "Budapest",
                  [Passenger("c", "c", "ER12456"), Passenger("c", "b", "PY12390"), Passenger("c", "a", "TR5690")]),
            Plane(4, "Airline4", 100, "Vienna",
                  [Passenger("d", "a", "WQ12456"), Passenger("d", "b", "TK12390"), Passenger("d", "c", "QS8790")])
        ])
        list = self.plane_repo.identify_planes_passport()
        self.assertEqual(list[0].getNumber(), 1)

        self.plane_repo.update_by_number(2, "Airline2", 80, "Paris",
                                         [Passenger("b", "a", "LJ12456"), Passenger("b", "b", "LJ12390")])
        list = self.plane_repo.identify_planes_passport()

        self.assertEqual(list[0].getNumber(), 1)
        self.assertEqual(list[1].getNumber(), 2)

        self.plane_repo.update_by_number(1, "Airline1", 180, "Rome",
                                         [Passenger("a", "a", "C12456"), Passenger("a", "b", "NC12390"),
                                          Passenger("a", "c", "NC10897")])
        list = self.plane_repo.identify_planes_passport()

        self.assertEqual(list[0].getNumber(), 2)

    def test_identify_passengers(self):
        '''

        :return:
        '''

        list = self.plane_repo.identify_passengers_c(1,
                                                   "a")  # we can check only the passport of the passenger because it is unique
        self.assertEqual(list[0].getPassport(), "NC12456")
        self.assertEqual(list[1].getPassport(), "AL12390")
        self.assertEqual(list[2].getPassport(), "OK90897")

        list = self.plane_repo.identify_passengers_c(3, "b")
        self.assertEqual(list[0].getPassport(), "PY12390")






