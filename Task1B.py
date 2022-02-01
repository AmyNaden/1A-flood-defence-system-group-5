from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
 

def run():
    '''Required for Task 1B'''

    # Build list of stations
    stations = build_station_list()

    # List of stations sorted by distance from Cambrdige city centre
    stations_sorted_list = stations_by_distance(stations, (52.2053, 0.1218))
    first_ten = stations_sorted_list[:10]
    last_ten = stations_sorted_list[-10:]

    # Print closest ten stations
    print(first_ten)

    # Print furthest ten stations
    print(last_ten)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()