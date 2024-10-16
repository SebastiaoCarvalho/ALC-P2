from z3 import Optimize, Not, Or, Implies
from domain.flight import Flight
from domain.city import City
from encoding.smt.encoder import Encoder

class StartInBaseCity(Encoder):

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City]) -> None:
        for city in city_dict.keys():
            if not city_dict[city].is_base_city():
                continue
            flights = [flight for flight in flight_list if flight.get_departure_city() != city]
            departs = [flight for flight in flight_list if flight.get_departure_city() == city]
            for depart in departs:
                for flight in flights:
                    solver.add(
                        Implies(
                            depart.get_day() >= flight.get_day(), 
                            Or(Not(depart.get_id()), Not(flight.get_id()))
                        )
                    )