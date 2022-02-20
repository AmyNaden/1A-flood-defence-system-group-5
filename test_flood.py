"""Unit test for the flood module"""
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():
    # Create two stations - one above and one below threshold
    station1 = MonitoringStation(0,0,0,0,(2.5,3.6),0,0)
    station2 = MonitoringStation(0,0,0,0,(2.5,3.6),0,0)
    station1.latest_level = 2.7
    station2.latest_level = 0.5
    # Add two stations to a list
    stations = [station1, station2]
    # Call function passing list and threshold value 0.8
    over_thresh = stations_level_over_threshold(stations, 0.8)
    assert over_thresh == [station1, 2.7]
