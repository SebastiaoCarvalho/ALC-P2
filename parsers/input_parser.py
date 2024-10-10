import sys
from domain.city import City
from domain.flight import Flight

from typing import Dict, List, Tuple

def parse_input() -> Tuple[Dict[str, City], List[Flight]]:
    city_map = {}
    flight_list = []
    n : int = int(readline())
    base_city = parse_base_city()
    city_map[base_city.code] = base_city
    for _ in range(n-1):
        city = parse_city()
        city_map[city.code] = city
    m : int = int(readline())
    for _ in range(m):
        flight_list = parse_flight(flight_list)
    for i in range(len(flight_list)):
        flight_list[i].id = i + 1
    return city_map, flight_list


def parse_base_city() -> City:
    city_info = readline()
    city_name, airport_code = city_info.split(' ')
    return City(city_name, airport_code, -1)

def parse_city() -> City:
    city_info = readline()
    city_name, airport_code, num_nights = city_info.split(' ')
    num_nights = int(num_nights)
    return City(city_name, airport_code, num_nights)

def readline() -> str:
    return sys.stdin.readline().strip()

def parse_flight(flight_list : list[Flight]) -> Flight:
    flight_info = readline()
    day, departure_city, arrival_city, departure_time, arrival_time, cost = flight_info.split()
    cost = int(cost)
    flight = Flight(0, day, departure_city, arrival_city, departure_time, arrival_time, cost)
    duplicates : list[Flight] = list(filter(lambda f : f.departure_city == flight.departure_city and f.arrival_city == flight.arrival_city and f.day == flight.day, flight_list))
    if len(duplicates) > 0:
        duplicates.append(flight)   
        #remove all duplicates from flight_list
        flight_list = list(filter(lambda f : f.departure_city != flight.departure_city or f.arrival_city != flight.arrival_city or f.day != flight.day, flight_list))
        min_cost = min(list(map(lambda f: f.cost, duplicates)))
        flight = Flight(0, day, departure_city, arrival_city, departure_time, arrival_time, min_cost)
    flight_list.append(flight)
    return flight_list
