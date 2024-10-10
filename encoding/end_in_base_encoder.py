from z3 import Optimize, Not, Or
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder

class EndInBaseEncoder(Encoder):

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int:
        for city in city_dict.keys():
            if not city_dict[city].is_base_city():
                continue
            arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
            flights  = [flight for flight in flight_list if flight.get_arrival_city() != city]
            for arrival in arrivals:
                for flight in flights:
                    if arrival.get_day() <= flight.get_day():
                        solver.add(Or(Not(arrival.get_id()), Not(flight.get_id())))
        return var_count