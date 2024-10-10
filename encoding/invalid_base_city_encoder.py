from datetime import timedelta
from z3 import Optimize
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder

class InvalidBaseCityEncoder(Encoder):

        def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int:
            nights = [city_dict[city].get_nights() for city in city_dict.keys() if not city_dict[city].is_base_city()]
            total_nights = sum(nights)
            for city in city_dict.keys():
                if not city_dict[city].is_base_city():
                    continue
                departs = [flight for flight in flight_list if flight.get_departure_city() == city]
                for depart in departs:
                     if depart.get_day() + timedelta(days=total_nights) > flight_list[-1].get_day():
                         solver.add([-depart.get_id()])
                arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
                for arrival in arrivals:
                    if arrival.get_day() - timedelta(days=total_nights) < flight_list[0].get_day():
                        solver.add([-arrival.get_id()])
            return var_count
                    
