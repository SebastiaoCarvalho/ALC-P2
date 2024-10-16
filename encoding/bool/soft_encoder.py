from z3 import Optimize, Not, If
from domain.flight import Flight
from domain.city import City
from encoding.bool.encoder import Encoder

class SoftEncoder(Encoder):

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City]) -> None:
        for flight in flight_list:
            solver.add_soft(Not(flight.get_id()), weight=flight.get_cost())