from datetime import timedelta
from z3 import Optimize, Not
from domain.flight import Flight
from domain.city import City
from encoding.bool.encoder import Encoder

class InvalidBaseCityEncoder(Encoder):

        def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City]) -> None:
            min_nights = [city_dict[city].get_min_nights() for city in city_dict.keys() if not city_dict[city].is_base_city()]
            min_total_nights = sum(min_nights)
            for city in city_dict.keys():
                if not city_dict[city].is_base_city():
                    continue
                departs = [flight for flight in flight_list if flight.get_departure_city() == city]
                for depart in departs:
                     if depart.get_day() + timedelta(days=min_total_nights) > flight_list[-1].get_day():
                         solver.add(Not(depart.get_id()))
                arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
                for arrival in arrivals:
                    if arrival.get_day() - timedelta(days=min_total_nights) < flight_list[0].get_day():
                        solver.add(Not(arrival.get_id()))