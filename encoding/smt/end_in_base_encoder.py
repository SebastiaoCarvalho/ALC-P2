from z3 import Optimize, Not, Or, Implies
from domain.flight import Flight
from domain.city import City
from encoding.smt.encoder import Encoder

class EndInBaseEncoder(Encoder):

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City]) -> None:
        for city in city_dict.keys():
            if not city_dict[city].is_base_city():
                continue
            arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
            flights  = [flight for flight in flight_list if flight.get_arrival_city() != city]
            for arrival in arrivals:
                for flight in flights:
                    solver.add(
                        Implies(
                            arrival.get_day() <= flight.get_day(), 
                            Or(Not(arrival.get_id()), Not(flight.get_id()))
                        )
                    )