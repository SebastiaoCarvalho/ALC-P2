from z3 import Optimize, Not, Or
from domain.flight import Flight
from domain.city import City
from encoding.bool.encoder import Encoder

class StartInBaseCity(Encoder):

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int:
        for city in city_dict.keys():
            if not city_dict[city].is_base_city():
                continue
            flights = [flight for flight in flight_list if flight.get_departure_city() != city]
            departs = [flight for flight in flight_list if flight.get_departure_city() == city]
            for depart in departs:
                for flight in flights:
                    if flight.get_day() <= depart.get_day():
                        solver.add(Or(Not(depart.get_id()), Not(flight.get_id())))
        return var_count