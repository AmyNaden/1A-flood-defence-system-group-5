# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#  Import relevant libraries 
from black import re_compile_maybe_verbose
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.station import MonitoringStation
from haversine import haversine # Used for calculating distance 

 
def stations_by_distance(stations, p):
    '''Required for task 1B - returns a list of stations and there distance from an arbitrary point p'''
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
        if all_stations[i][2] <= r:
            found_stations.append(all_stations[i][0])
    return found_stations

def rivers_with_station(stations):
    '''Required for task 1D - returns names of rivers with a monitoring station'''
    # Define an empty set for river names
    rivers = set()
    # Loop through each station object 
    for i in range(len(stations)):
        # Add river name to set 
        rivers.add(stations[i].river)
    return rivers 

def stations_by_river(stations):
    '''Required for task 1D - returns a dictionary that maps river names to a list of station objects on given river'''
    # Define empty dictionary 
    rivers_dict = {}
    # Loop through each station object
    for i in range(len(stations)):
        river_key = stations[i].river # Use river name as dictionary key
        # assign list of stations to correct river in dictionary 
        if river_key not in rivers_dict.keys():
            station_list = [stations[i]]
            rivers_dict[river_key] = station_list
        else:
            station_list = rivers_dict[river_key] # Find existing station list
            station_list.append(stations[i]) # Add new station to list
            rivers_dict[river_key] = station_list
    # Return completed dictionary 
    return rivers_dict

def station_names(stations):
    '''Return the names of station in alphebetical order from list of station objects'''
    # Define empty list of station names
    station_names = []
    # Loop through each station object
    for i in range(len(stations)):
        # Add station name to list
        station_names.append(stations[i].name)
    # Return sorted list of names 
    station_names.sort()
    return station_names

def rivers_by_station_number(stations, N):
    '''Required for Task 1E - returns a list of rivers sorted by their number of stations'''
    # Fetch rivers dictionary
    rivers_dict = stations_by_river(stations)
    rivers_and_stations = []
    # Loop through each station object
    for i in range(len(rivers_dict)):
        # Extracts ith river from dictionary
        river = list(rivers_dict)[i-1]
        # Finds number of stations on river
        number_of_stations = len(rivers_dict[river])
        river_and_stations = (river, number_of_stations)
        # Adding (river, no. stations) tuple to list
        rivers_and_stations.append(river_and_stations)
    # Sort the list dependent on amount of stations
    sorted_rivers = sorted(rivers_and_stations, key=lambda tup: tup[1], reverse = True)
    # Define new list to cumulate all terms
    required_list = sorted_rivers[:N]
    # Iterate between the Nth term and the end of the list 
    for i in range(N-1, len(sorted_rivers)):
        # Iterate through these to find if any of them are the same as the Nth value
        if sorted_rivers[i][1] == sorted_rivers[N][1]: 
            required_list.append(sorted_rivers[i]) 
    return required_list
