'''plots the water levels over the past 10 days for the 5 stations at which the current relative water level is greatest.'''

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels, plot_water_levels_general
from floodsystem.datafetcher import fetch_measure_levels


def run1():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get list of station objects with top 5 relative water level
    top5 = stations_highest_rel_level(stations, 5)

    for i in range(5):
        station = top5[i][0]
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)

def run2():
    '''Extension - Test plot_water_level_general'''
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get list of station objects with top 5 relative water level
    N = 5
    topN = stations_highest_rel_level(stations, N)

    # Create list of station objects
    stations = []
    for i in range(N):
        stations.append(topN[i][0])
    
    plot_water_levels_general(stations)



if __name__ == "__main__":
    print("\n*** Task 2C: CUED Part IA Flood Warning System ***")
    run1()
    print("\n*** Task 2C Extension: CUED Part IA Flood Warning System ***")
    run2()
