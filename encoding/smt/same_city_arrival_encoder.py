from z3 import Optimize
from domain.flight import Flight
from domain.city import City
from encoding.smt.encoder import Encoder
from z3 import AtMost, AtLeast

class SameCityArrivalEncoder(Encoder) :

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City]) -> None:
        for city in city_dict.keys():
            arrivals = [flight.get_id() for flight in flight_list if flight.get_arrival_city() == city]
            solver.add(AtMost(arrivals + [1]))
            solver.add(AtLeast(arrivals + [1]))
    