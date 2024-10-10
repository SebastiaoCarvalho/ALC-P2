from z3 import Optimize, Or, Not
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder
from datetime import timedelta

class StayNDaysEncoder(Encoder) :

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int :
        for city in city_dict.keys():
            if city_dict[city].is_base_city():
                continue
            arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
            departs = [flight for flight in flight_list if flight.get_departure_city() == city]
            for arrival in arrivals:
                min_date = arrival.get_day() + timedelta(days=city_dict[city].get_min_nights())
                max_date = arrival.get_day() + timedelta(days=city_dict[city].get_max_nights())
                disjunction = [Not(arrival.get_id())]
                for depart in departs:
                    if min_date <= depart.get_day() <= max_date:
                        disjunction.append(depart.get_id())
                    else :
                        solver.add(Or(Not(arrival.get_id()), Not(depart.get_id()))) # can't stay either min or max nights
                solver.add(Or(disjunction))
        return var_count