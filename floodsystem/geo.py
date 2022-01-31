# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#  task B and C
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.station import MonitoringStation
import haversine
 
def stations_by_distance(stations, p):
    '''This function is required for task 1B'''
    '''This function returns a list of stations and there distance from an arbitrary point p'''
    stations_with_distance = []
    for i in range(len(stations)):
        distance = float(haversine(p, stations[i].coord))
        stations_with_distance.append(stations[i].name, stations[i].town, distance)
    stations_with_distance = sorted_by_key(stations_with_distance, 2, reverse=False)
    return stations_with_distance

def stations_within_radius(stations, centre, r):
    '''Required for task 1C - returns list of stations inside radius'''
    found_stations = []
    all_stations = stations_by_distance(stations, centre)
    for i in range(len(all_stations)):
        if all_stations[i](1) <= r:
            found_stations.append(all_stations[i](0))