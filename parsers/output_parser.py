from domain.flight import Flight
from domain.city import City

def parse_output(solution : list[int], flight_list : list[Flight], city_dict : dict[str, City]):
    print(solution)
    flight_list = [flight for flight in flight_list if solution[flight.get_id()]]
    flight_list.sort(key=lambda x: x.get_day())
    total_cost = sum(flight.get_cost() for flight in flight_list)
    print(total_cost)
    for flight in flight_list:
        print(parse_flight(flight, city_dict))
    return

def parse_flight(flight : Flight, city_dict : dict[str, City]):
    return f"{flight.convert_day_to_output()} {city_dict[flight.get_departure_city()].get_name()} {city_dict[flight.get_arrival_city()].get_name()} {flight.get_departure_time()} {flight.get_cost()}"