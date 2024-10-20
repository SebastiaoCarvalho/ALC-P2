#!/usr/bin/python3
# alc24 - 6 - project2

from parsers.input_parser import parse_input
from parsers.output_parser import parse_output
from z3 import Optimize, sat
from encoding.bool.same_city_depart_encoder import SameCityDepartEncoder
from encoding.bool.same_city_arrival_encoder import SameCityArrivalEncoder  
from encoding.bool.stay_n_days_encoder import StayNDaysEncoder
from encoding.bool.invalid_base_city_encoder import InvalidBaseCityEncoder
from encoding.bool.invalid_flights_encoder import InvalidFlightsEncoder
from encoding.bool.end_in_base_encoder import EndInBaseEncoder
from encoding.bool.start_in_base_city import StartInBaseCity
from encoding.bool.soft_encoder import SoftEncoder


city_map, flight_list = parse_input()

solver = Optimize()

# encoder = CityEncoder()
# var_counter = encoder.encode(solver, flight_list, city_map)

encoder = SameCityDepartEncoder()
encoder.encode(solver, flight_list, city_map)

encoder = SameCityArrivalEncoder()
encoder.encode(solver, flight_list, city_map)

encoder = StayNDaysEncoder()
encoder.encode(solver, flight_list, city_map)

encoder = EndInBaseEncoder()
encoder.encode(solver, flight_list, city_map)

encoder = StartInBaseCity()
encoder.encode(solver, flight_list, city_map)

encoder = InvalidFlightsEncoder()
encoder.encode(solver, flight_list, city_map)

encoder = InvalidBaseCityEncoder()
encoder.encode(solver, flight_list, city_map)

encoder = SoftEncoder()
encoder.encode(solver, flight_list, city_map)

if solver.check() == sat:
    parse_output(solver.model(), flight_list, city_map)
else:
    print(solver.unsat_core())
    print("No solution found")
