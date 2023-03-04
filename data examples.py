from domain.Plane import Plane
from domain.Passenger import Passenger
from Repository.Airport import PlaneRepository

#data examples for the first iteration

P1 = Passenger("Name1", "Name2", "Passport1")
P2 = Passenger("Name3", "Name3", "Passport2")
Plane1 = Plane(1, "Airline", 100, "destination", [Passenger("Name1", "Name2", "Passport1")])
Plane2 = Plane(2, "Airline2", 100, "destination2", [Passenger("Name3", "Name3", "Passport2")])
P1.getPassport()
P1.getLastName()
P2.getFirstName()
Plane1.getDestination()
Plane2.getList()
Plane2.delete_by_passport(passport = "Passport1")
Plane1.getDestination()
Plane2.getNumberSeats()

#data examples for the second iteration

MyPlanes = PlaneRepository([Plane(1, "w", 180, "Rome", [Passenger("a", "a", "12456"), Passenger("b", "b", "12390"),Passenger("c", "b", "90")]),
                            Plane(2, "w", 90, "Prague", [Passenger("b", "mao", "125678"), Passenger("ionela", "mara", "12390"), Passenger("ionel", "marin", "12")]),
                            Plane(3, "a", 90, "Prague", [Passenger("b", "mao", "125678"), Passenger("ionela", "mara", "12390"), Passenger("ionel", "marin", "12")])
                            ])


MyPlanes.get_planes()
MyPlanes.sort_planes_acc_to_concatenation()
MyPlanes.sort_by_substring("ion")
MyPlanes.identify_planes_passport()


#data examples for the third
MyPlanes.groupPlanes(2)
MyPlanes.groupPersons(1, 2)
MyPlanes.groupPlanes(3)