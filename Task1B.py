from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
 
stations = build_station_list()
print(len(stations))
stations_sorted_list = stations_by_distance(stations, (52.2053, 0.1218))
first_ten = stations_sorted_list[0:9]
last_ten = stations_sorted_list[:10]
print(first_ten)
print(last_ten)