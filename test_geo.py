"""Unit test for the geo module"""

from floodsystem.geo import stations_within_radius, rivers_with_station, stations_by_river, stations_by_distance 
from floodsystem.stationdata import build_station_list 

def test_stations_by_distance():
    # Build list of stations and define coord
    stations = build_station_list()
    p = 52.2053, 0.1218
    # Call function being tested
    by_distance = stations_by_distance(stations, p)
    # Type and length checks
    assert isinstance(by_distance, list)
    assert len(by_distance) > 0
    assert isinstance(by_distance[0], tuple)

def test_stations_within_radius():
    # Build list of stations
    stations = build_station_list()
    # Find stations within 10km radius of Cambridge
    found_stations = stations_within_radius(stations, (52.2053, 0.1218), 10)
    # Type and length checks
    assert isinstance(found_stations, list)
    assert len(found_stations) > 0

def test_rivers_with_station():
    # Build list of stations
    stations = build_station_list()
    # Call function being tested
    rivers = rivers_with_station(stations)
    assert isinstance(rivers, set)
    assert len(rivers)

def test_stations_by_river():
    # Build list of stations
    stations = build_station_list()
    # Call function being tested
    rivers = stations_by_river(stations)
    assert len(rivers) > 0
