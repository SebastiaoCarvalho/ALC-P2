#!/usr/bin/python3
# alc24 - 6 - project2

from parsers.input_parser import parse_input
from parsers.output_parser import parse_output
from z3 import Optimize, sat
from encoding.smt.same_city_depart_encoder import SameCityDepartEncoder
from encoding.smt.same_city_arrival_encoder import SameCityArrivalEncoder  
from encoding.smt.stay_n_days_encoder import StayNDaysEncoder
from encoding.smt.end_in_base_encoder import EndInBaseEncoder
from encoding.smt.start_in_base_city import StartInBaseCity
from encoding.smt.soft_encoder import SoftEncoder
from encoding.smt.invalid_flights_encoder import InvalidFlightsEncoder
from encoding.smt.invalid_base_city_encoder import InvalidBaseCityEncoder
from encoding.smt.city_encoder import CityEncoder


city_map, flight_list = parse_input()

solver = Optimize()

encoder = CityEncoder()
var_counter = encoder.encode(solver, flight_list, city_map)

encoder = SameCityDepartEncoder()
var_counter = encoder.encode(solver, flight_list, city_map)

encoder = SameCityArrivalEncoder()
var_counter = encoder.encode(solver, flight_list, city_map)

encoder = StayNDaysEncoder()
var_counter = encoder.encode(solver, flight_list, city_map)

encoder = EndInBaseEncoder()
var_counter = encoder.encode(solver, flight_list, city_map)

encoder = StartInBaseCity()
var_counter = encoder.encode(solver, flight_list, city_map)

encoder = SoftEncoder()
var_counter = encoder.encode(solver, flight_list, city_map)

encoder = InvalidFlightsEncoder()
var_counter = encoder.encode(solver, flight_list, city_map)

encoder = InvalidBaseCityEncoder()
var_counter = encoder.encode(solver, flight_list, city_map)

if solver.check() == sat:
    parse_output(solver.model(), flight_list, city_map)
else:
    print(solver.unsat_core())
    print("No solution found")
