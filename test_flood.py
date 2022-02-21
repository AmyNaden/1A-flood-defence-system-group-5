"""Unit test for the flood module"""
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import update_water_levels, build_station_list

def test_stations_level_over_threshold():
    # Create two stations - one above and one below threshold
    station1 = MonitoringStation(0,0,0,0,(2.5,3.6),0,0)
    station2 = MonitoringStation(0,0,0,0,(2.5,3.6),0,0)
    station1.latest_level = 2.7
    station2.latest_level = 0.5
    # Add two stations to a list
    stations = [station1, station2]
    # Call function passing list and threshold value 0.16
    over_thresh = stations_level_over_threshold(stations, 0.16)
    assert len(over_thresh) == 1
    assert over_thresh[0][0] == station1

def test_stations_highest_rel_level():
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)
    # Get list of station objects with top N relative water level
    N = 5
    topN = stations_highest_rel_level(stations, N)
    # Check list is the correct length
    assert len(topN) == N
    # Check first item in list is a tuple
    assert isinstance(topN[0], tuple)
    # Check list is in descending order
    assert topN[0][1] > topN[1][1]
