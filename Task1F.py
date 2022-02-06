from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def run():
    # Building list of stations
    stations = build_station_list()
    # Using function to get a list of stations with inconsistent range datas
    list = inconsistent_typical_range_stations(stations)
    # Sorting to alphabetical
    list.sort()
    print(list)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
