from z3 import Optimize
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder
from z3 import AtMost, AtLeast

class SameCityDepartEncoder(Encoder) :

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int :
        for city in city_dict.keys():
            departs = [flight.get_id() for flight in flight_list if flight.get_departure_city() == city]
            solver.add(AtMost(departs + [1]))
            solver.add(AtLeast(departs + [1]))
        return var_count