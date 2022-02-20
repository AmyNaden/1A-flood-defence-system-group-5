# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations 


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_monitoring_station_method():
    # Creating three stations known to be consistent or inconsistent
    inconsistent = MonitoringStation(0, 0, 0, 0, (3.6, 2.5), 0, 0)
    no_range = MonitoringStation(0, 0, 0, 0, None, 0, 0)
    consistent = MonitoringStation(0, 0, 0, 0, (1.5, 3.4), 0, 0)

    assert MonitoringStation.typical_range_consistent(inconsistent) == False
    assert MonitoringStation.typical_range_consistent(no_range) == False
    assert MonitoringStation.typical_range_consistent(consistent) == True

def test_inconsistent_typical_range_stations():
    # Creating three stations known to be consistent or inconsistent 
    inconsistent = MonitoringStation(0, 0, 0, 0, (3.6, 2.5), 0, 0)
    no_range = MonitoringStation(0, 0, 0, 0, None, 0, 0)
    consistent = MonitoringStation(0, 0, 0, 0, (1.5, 3.4), 0, 0)
    stations = [inconsistent, no_range, consistent]
    
    assert inconsistent_typical_range_stations(stations) == [inconsistent.name, no_range.name]

def test_relative_water_level():
    # Creating station with ratio 1
    station1 = MonitoringStation(0,0,0,0,(2.5,3.6),0,0)
    station1.latest_level = 3.6
    assert station1.relative_water_level() == 1.0
    # Creating station with ratio 0
    station2 = MonitoringStation(0,0,0,0,(2.5,3.6),0,0)
    station2.latest_level = 2.5
    assert station2.relative_water_level() == 0.0
    # Creating station with no data available
    station3 = MonitoringStation(0,0,0,0,(2.5,3.6),0,0)
    station3.latest_level = None
    assert station3.relative_water_level() == None
    # Creating station with inconsitent data 
    station4 = MonitoringStation(0,0,0,0,(3.6,2.5),0,0)
    station4.latest_level = 2.5
    assert station4.relative_water_level() == None
