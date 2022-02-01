# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#  Import relevant libraries 
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.station import MonitoringStation
from haversine import haversine # Used for calculating distance 

 
def stations_by_distance(stations, p):
    '''This function is required for task 1B'''
    '''This function returns a list of stations and there distance from an arbitrary point p'''
    # Define empty list 
    stations_with_distance = []
    # Loop through each station object 
    for i in range(len(stations)):
        # Calculate distance between station and specified location
        distance = haversine(p, stations[i].coord)
        # Create list with stations name, down and distance
        info = (stations[i].name, stations[i].town, distance)
        stations_with_distance.append(info)
    # Sort list of stations by distance 
    stations_with_distance = sorted_by_key(stations_with_distance, 2, reverse=False)
    return stations_with_distance

def stations_within_radius(stations, centre, r):
    '''Required for task 1C - returns list of stations inside radius'''
    # Define empty list
    found_stations = []
    # Find distance of each station from specified point
    all_stations = stations_by_distance(stations, centre)
    # Loop through each station object
    for i in range(len(all_stations)):
        # If station is inside radius add it to the list found_stations
        if all_stations[i](2) <= r:
            found_stations.append(all_stations[i](0))
    return found_stations