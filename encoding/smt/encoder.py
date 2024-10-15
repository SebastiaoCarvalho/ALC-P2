from z3 import Optimize
from domain.flight import Flight
from domain.city import City

class Encoder :

    @staticmethod
    def encode(self, solver : Optimize, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> None :
        pass

