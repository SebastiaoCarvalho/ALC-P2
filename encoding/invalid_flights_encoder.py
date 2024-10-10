from datetime import timedelta
from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder

class InvalidFlightsEncoder(Encoder):

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int:

        for city in city_dict.keys():
            if city_dict[city].is_base_city():
                continue
            required_stay = city_dict[city].get_nights()
            arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
            departs = [flight for flight in flight_list if flight.get_departure_city() == city]
            for depart in departs:
                required_arrival_day = depart.get_day() - timedelta(days=required_stay)
                if not any(arrival.get_day() == required_arrival_day for arrival in arrivals):
                    solver.add_clause([-depart.get_id()])
                