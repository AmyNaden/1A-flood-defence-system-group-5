import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit

def run():
    # Fetching list of stations and updating water levels
    stations = build_station_list()
    update_water_levels(stations)
    # Getting stations with 5 highest relative water levels
    top5 = stations_highest_rel_level(stations, 5)
    # Iterating through these 5 stations
    for i in range(len(top5)):
        # Fetching the data for various times in the past 2 days
       dates = fetch_measure_levels(top5[i][0].measure_id, dt=datetime.timedelta(days=2))[0]
       levels = fetch_measure_levels(top5[i][0].measure_id, dt=datetime.timedelta(days=2))[1]
       # Plotting a graph using this data
       plot_water_level_with_fit(top5[i][0], dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()