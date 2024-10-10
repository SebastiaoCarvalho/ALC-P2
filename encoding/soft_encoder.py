from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder

class SoftEncoder(Encoder):

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int :
        for flight in flight_list:
            solver.add_clause([-flight.get_id()], weight=flight.get_cost())