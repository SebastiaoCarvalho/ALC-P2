from datetime import timedelta
from z3 import Optimize, Not, Implies
from domain.flight import Flight
from domain.city import City
from encoding.smt.encoder import Encoder

class InvalidBaseCityEncoder(Encoder):

        def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City]) -> None:
            nights = [city_dict[city].get_var() for city in city_dict.keys() if not city_dict[city].is_base_city()]
            total_nights = sum(nights)
            for city in city_dict.keys():
                if not city_dict[city].is_base_city():
                    continue
                departs = [flight for flight in flight_list if flight.get_departure_city() == city]
                for depart in departs:
                    solver.add(
                        Implies(
                            depart.get_day() + total_nights > flight_list[-1].get_day(),
                            Not(depart.get_id())
                        )
                     )
                arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
                for arrival in arrivals:
                    solver.add(
                        Implies(
                            arrival.get_day() - total_nights < flight_list[0].get_day(),
                            Not(arrival.get_id())
                        )
                    )