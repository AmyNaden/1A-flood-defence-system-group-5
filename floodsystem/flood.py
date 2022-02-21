from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    '''Required for task 2B - returns list of tuples for stations with relative level over threshold value'''
    # Define empty list
    stations_over_thresh = []
    # Loop through all stations
    for i in range(len(stations)):
        relative_level = stations[i].relative_water_level()
        # Don't do anything if data is inconsistent
        if relative_level != None:
            # Add tuple to list for stations with relative level above threshold
            if relative_level > tol:
                station = (stations[i], relative_level)
                stations_over_thresh.append(station)
    # Sort list by relative level in descending order
    stations_over_thresh.sort(key=lambda x:x[1], reverse=True)
    # Return list 
    return stations_over_thresh

def stations_highest_rel_level(stations, N):
    '''Required for task 2C - returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest. '''
    # Gets list of stations in order of relative level
    stations_relative_level = stations_level_over_threshold(stations, 0)
    # Create list of first N stations
    topN_stations = stations_relative_level[0:N]
    return topN_stations


