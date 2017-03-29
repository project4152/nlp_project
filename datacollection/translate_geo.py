"""
translate city listed in the state-city file into longitude and latitude
"""
from geopy.geocoders import Nominatim

def translate(filename):
    """
    translate city into longitude and latitude
    :param filename:
    :return:
    """
    state_city_map = dict()
    geolocator = Nominatim()
    with open(filename, "r")as f:
        for state_city in f.readlines():
            state_city = state_city.strip()
            # print state_city.split("-")
            if state_city != "":
                state_city_tuple = state_city.split("-")
                state_city_map[state_city_tuple[0]] = geolocator.geocode(state_city_tuple[1])

    f.close()
    return  state_city_map
