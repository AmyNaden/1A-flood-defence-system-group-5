from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get list of station objects with top 10 relative water level
    top10 = stations_highest_rel_level(stations, 10)

    # Print name and relative level of each station in list
    for i in range(10):
        name = top10[i][0].name
        relative_level = top10[i][1]
        print(name, relative_level)

if __name__ == "__main__":
    print("\n*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
