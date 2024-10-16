from z3 import Optimize, Or, Not, Implies
from domain.flight import Flight
from domain.city import City
from encoding.smt.encoder import Encoder
from datetime import timedelta

class StayNDaysEncoder(Encoder) :

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City]) -> None:
        for city in city_dict.keys():
            if city_dict[city].is_base_city():
                continue
            arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
            departs = [flight for flight in flight_list if flight.get_departure_city() == city]
            for arrival in arrivals:
                for depart in departs:
                    solver.add(
                        Implies(
                            (depart.get_day() - arrival.get_day()).days != city_dict[city].get_var(),  
                            Or(Not(depart.get_id()), Not(arrival.get_id()))
                        )
                    )