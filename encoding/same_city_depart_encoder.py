from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder
from pysat.card import CardEnc, EncType

class SameCityDepartEncoder(Encoder) :

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int :
        for city in city_dict.keys():
            departs = [flight.get_id() for flight in flight_list if flight.get_departure_city() == city]
            enc = CardEnc.equals(departs, bound=1, top_id=var_count, encoding=EncType.seqcounter)
            for clause in enc.clauses:
                solver.add_clause(clause)
            var_count = max(var_count, max(abs(literal) for clause in enc.clauses for literal in clause))
        return var_count