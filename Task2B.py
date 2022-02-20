from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels


def run():
    # Build list of stations
    stations = build_station_list()
    # Fetch latest water levels
    update_water_levels(stations)
    # Get list of stations where current relative level is over 0.8
    stations_over_thresh = stations_level_over_threshold(stations, 0.8)
    # Print name of station and current relative level
    for i in range(len(stations_over_thresh)):
        name = stations_over_thresh[i][0].name
        relative_level = stations_over_thresh[i][1]
        print(name, relative_level)

if __name__ == "__main__":
    print("\n*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
