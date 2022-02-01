from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius 


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Find stations within 10km radius of Cambridge
    found_stations = stations_within_radius(stations, (52.2053, 0.1218), 10)

    # Print stations in alphabetical order
    print(found_stations.sort())
    

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()