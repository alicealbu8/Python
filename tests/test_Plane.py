from unittest import TestCase
from domain.Plane import Plane
from domain.Passenger import Passenger
class TestPlane(TestCase):
    '''

    '''
    def setUp(self):
        self.plane = Plane(1, "Airline", 30, "Destination",   [Passenger("a", "a", "123"), Passenger("b", "b", "124"), Passenger("c", "c", "125")])
    def test_create(self):
        #test getters
        self.assertEqual(self.plane.getNumber(), 1)
        self.assertEqual(self.plane.getAirline(), "Airline")
        self.assertEqual(self.plane.getNumberSeats(), 30)
        list = self.plane.getList()
        self.assertEqual(list[0].getFirstName(), "a")
        self.assertEqual(list[0].getLastName(), "a")
        self.assertEqual(list[0].getPassport(), "123")
        self.assertEqual(list[1].getFirstName(), "b")
        self.assertEqual(list[1].getLastName(), "b")
        self.assertEqual(list[1].getPassport(), "124")
        self.assertEqual(list[2].getFirstName(), "c")
        self.assertEqual(list[2].getLastName(), "c")
        self.assertEqual(list[2].getPassport(), "125")

        #testsetters

        self.plane.setNumber(2)
        self.assertEqual(self.plane.getNumber(), 2)
        self.plane.setAirline("Airline2")
        self.assertEqual(self.plane.getAirline(), "Airline2")
        self.plane.setNumberSeats(20)
        self.assertEqual(self.plane.getNumberSeats(), 20)
        self.plane.setList([Passenger("aa", "a", "123"), Passenger("bb", "b", "124"), Passenger("cc", "c", "125")])
        list = self.plane.getList()
        self.assertEqual(list[0].getFirstName(), "aa")
        self.assertEqual(list[0].getLastName(), "a")
        self.assertEqual(list[0].getPassport(), "123")
        self.assertEqual(list[1].getFirstName(), "bb")
        self.assertEqual(list[1].getLastName(), "b")
        self.assertEqual(list[1].getPassport(), "124")
        self.assertEqual(list[2].getFirstName(), "cc")
        self.assertEqual(list[2].getLastName(), "c")
        self.assertEqual(list[2].getPassport(), "125")

        # test if value is raised when type if number of seats is negative
        try:
            P = Plane(1, "Airline", -30, "Destination",   [Passenger("a", "a", "123"), Passenger("b", "b", "124"), Passenger("c", "c", "125")])
            self.assertFalse(True)
        except ValueError as ver:
            self.assertTrue(True)

        try:
            self.plane.setNumberSeats(-30)
            self.assertFalse(True)
        except ValueError as ver:
            self.assertTrue(True)

        # we check Number every time to be sure that it is not changing

        self.plane.setAirline("Airline2")
        self.assertEqual(self.plane.getNumber(), 2)
        self.plane.setNumberSeats(20)
        self.assertEqual(self.plane.getNumber(), 2)
        self.plane.setList([Passenger("aa", "a", "123"), Passenger("bb", "b", "124"), Passenger("cc", "c", "125")])
        self.assertEqual(self.plane.getNumber(), 2)

    def test_operations(self):

        #test function add_passenger

        self.plane.add_passenger("aa", "bb", "1234")
        list = self.plane.getList()
        self.assertEqual(list[3].getFirstName(), "aa")
        self.assertEqual(list[3].getLastName(), "bb")
        self.assertEqual(list[3].getPassport(), "1234")

        self.plane.add_passenger("ab", "bc", "12345")

        self.assertEqual(list[4].getFirstName(), "ab")
        self.assertEqual(list[4].getLastName(), "bc")
        self.assertEqual(list[4].getPassport(), "12345")

        #test if an error is raised when adding a person with the same passport number

        try:
            self.plane.add_passenger("abc", "abc", "1234")
            self.assertFalse(True)
        except ValueError as ver:
            self.assertTrue(True)

        #test function update by passport

        self.plane.update_by_passport("123", "d", "d")

        self.assertEqual(list[0].getFirstName(), "d")
        self.assertEqual(list[0].getLastName(), "d")
        self.assertEqual(list[0].getPassport(), "123")

        self.plane.update_by_passport("124", "d", "d")

        self.assertEqual(list[1].getFirstName(), "d")
        self.assertEqual(list[1].getLastName(), "d")
        self.assertEqual(list[1].getPassport(), "124")

        #test function delete by passport

        self.plane.delete_by_passport("123")

        self.assertEqual(list[0].getFirstName(), "d")
        self.assertEqual(list[0].getLastName(), "d")
        self.assertEqual(list[0].getPassport(), "124")

        self.plane.delete_by_passport("124")

        self.assertEqual(list[0].getFirstName(), "c")
        self.assertEqual(list[0].getLastName(), "c")
        self.assertEqual(list[0].getPassport(), "125")










