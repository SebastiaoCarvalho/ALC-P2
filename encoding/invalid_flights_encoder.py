from datetime import timedelta
from z3 import Optimize, Or, Not
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder

class InvalidFlightsEncoder(Encoder):

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int:

        for city in city_dict.keys():
            if city_dict[city].is_base_city():
                continue
            arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
            departs = [flight for flight in flight_list if flight.get_departure_city() == city]
            for depart in departs:
                max_date = depart.get_day() - timedelta(days=city_dict[city].get_min_nights())
                min_date = depart.get_day() - timedelta(days=city_dict[city].get_max_nights())
                if not any((arrival.get_day() <= max_date and arrival.get_day() >= min_date) for arrival in arrivals):
                    print("Invalid flight", max_date, min_date)
                    print(depart.get_id())
                    solver.add(Not(depart.get_id()))
                