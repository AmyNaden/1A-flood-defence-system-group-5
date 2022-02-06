from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import station_names 
from floodsystem.geo import rivers_by_station_number

def run():
    # Builds list of stations
    stations = build_station_list()
    N = 9
    # Using function to get first N stations
    list = rivers_by_station_number(stations, N)
    # Printing 
    print("\nThe 9 rivers with the greatest number of monitoring stations - ", list)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()