from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City

class Encoder :

    @staticmethod
    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> None :
        pass

