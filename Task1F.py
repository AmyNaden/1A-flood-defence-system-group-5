from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    list = inconsistent_typical_range_stations(stations)
    print(list)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
