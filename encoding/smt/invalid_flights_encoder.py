from datetime import timedelta
from z3 import Optimize, Not, And, Implies
from domain.flight import Flight
from domain.city import City
from encoding.smt.encoder import Encoder

class InvalidFlightsEncoder(Encoder):

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int:
        for city in city_dict.keys():
            if city_dict[city].is_base_city():
                continue
            arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
            departs = [flight for flight in flight_list if flight.get_departure_city() == city]
            for depart in departs:
                clauses = []
                for arrival in arrivals:
                    clauses += [(depart.get_day() - arrival.get_day()).days != city_dict[city].get_var()]
                solver.add(
                    Implies(
                        And(clauses),
                        Not(depart.get_id())
                    )
                )
                