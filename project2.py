#!/usr/bin/python3
# alc24 - 6 - project1 

from parsers.input_parser import parse_input
from parsers.output_parser import parse_output
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF
from encoding.same_city_depart_encoder import SameCityDepartEncoder
from encoding.same_city_arrival_encoder import SameCityArrivalEncoder  
from encoding.stay_n_days_encoder import StayNDaysEncoder
from encoding.end_in_base_encoder import EndInBaseEncoder
from encoding.start_in_base_city import StartInBaseCity
from encoding.soft_encoder import SoftEncoder
from encoding.invalid_flights_encoder import InvalidFlightsEncoder
from encoding.invalid_base_city_encoder import InvalidBaseCityEncoder


city_map, flight_list = parse_input()

solver = RC2(WCNF())

encoder = SameCityDepartEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, len(flight_list))

encoder = SameCityArrivalEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

encoder = StayNDaysEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

encoder = EndInBaseEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

encoder = StartInBaseCity()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

encoder = SoftEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

encoder = InvalidFlightsEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

encoder = InvalidBaseCityEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

solution = solver.compute()
if solution != None:
    parse_output(solution, flight_list, city_map)
