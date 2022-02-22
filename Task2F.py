import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit

stations = build_station_list()

update_water_levels(stations)

top5 = stations_highest_rel_level(stations, 5)

for i in range(len(top5)):
   dates, levels = fetch_measure_levels(top5[i].measure_id, dt=datetime.timedelta(days=2))
   plot_water_level_with_fit(top5[i].name, dates, levels, 4)