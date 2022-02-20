# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        '''Required for Task 1F - finds inconsistent range data'''
        # Case where there is no data
        if self.typical_range == None:
            return False
        # If high value less than low value then inconsistent
        elif (self.typical_range[1] < self.typical_range[0]):
            return False
        # Otherwise must be true
        else:
            return True
    
    def relative_water_level(self):
        '''Required for task 2B - returns the latest water level as a fraction of the typical range'''
        # If data is not available return None
        if self.latest_level == None:
            return None
        # If data is inconsistent return None
        elif self.typical_range_consistent() == False:
            return None
        # If data is available and consistent return ratio
        else:
            ratio = (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])
            # Additional check to remove unrealistic data
            if ratio < 50:
                return ratio
            else:
                return None

def inconsistent_typical_range_stations(stations):
    '''Required for Task 1F - prints a list of inconsistent data'''
    # Creates an list to fill with inconsistent stations
    inconsistent_stations = []
    # Iterates through the stations
    for station in stations:
        # Uses class method to find inconsistent data
        if MonitoringStation.typical_range_consistent(station) == False:
            # Adds the inconsistent stations to the list
            inconsistent_stations.append(station.name)
    return inconsistent_stations





