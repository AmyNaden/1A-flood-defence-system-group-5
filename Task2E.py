'''plots the water levels over the past 10 days for the 5 stations at which the current relative water level is greatest.'''

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get list of station objects with top 5 relative water level
    top10 = stations_highest_rel_level(stations, 5)

    for i in range(5):
        station = top10[i][0]
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("\n*** Task 2C: CUED Part IA Flood Warning System ***")
    run()