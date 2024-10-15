from z3 import Optimize
from domain.flight import Flight
from domain.city import City

class CityEncoder :

    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> None :
        for city in city_dict.values():
            if city.is_base_city():
                continue
            solver.add(city.get_min_nights() <= city.get_var())
            solver.add(city.get_var() <= city.get_max_nights())
        return var_count

