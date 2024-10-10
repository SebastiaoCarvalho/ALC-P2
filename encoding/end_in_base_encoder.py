from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder

class EndInBaseEncoder(Encoder):

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int:
        for city in city_dict.keys():
            if not city_dict[city].is_base_city():
                continue
            arrivals = [flight.get_id() for flight in flight_list if flight.get_arrival_city() == city]
            flights  = [flight.get_id() for flight in flight_list if flight.get_arrival_city() != city]
            for arrival in arrivals:
                for flight in flights:
                    if flight_list[arrival - 1].get_day() <= flight_list[flight - 1].get_day():
                        solver.add_clause([-arrival, -flight])
        return var_count