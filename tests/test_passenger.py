from unittest import TestCase
from domain.Passenger import Passenger
class TestPassenger(TestCase):

    def setUp(self):
        self.passenger = Passenger("FirstName", "LastName", "Passport1")

    def test_create(self):
        #test getters
        self.assertEqual(self.passenger.getLastName(), "LastName")
        self.assertEqual(self.passenger.getFirstName(), "FirstName")
        self.assertEqual(self.passenger.getPassport(), "Passport1")

        #test setters
        self.passenger.setFirstName("FirstName2")
        self.assertEqual(self.passenger.getFirstName(), "FirstName2")
        self.passenger.setLastName("LastName2")
        self.assertEqual(self.passenger.getLastName(), "LastName2")
        self.passenger.setPassport("Passport2")
        self.assertEqual(self.passenger.getPassport(), "Passport2")

        # we check passport every time to be sure that it is not changing
        self.passenger.setFirstName("FirstName2")
        self.assertEqual(self.passenger.getPassport(), "Passport2")
        self.passenger.setLastName("LastName2")
        self.assertEqual(self.passenger.getPassport(), "Passport2")


