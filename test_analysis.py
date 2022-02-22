from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
import numpy

def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)
    a_station = stations[52]
    dates = fetch_measure_levels(a_station.measure_id, dt=datetime.timedelta(days=2))[0]
    levels = fetch_measure_levels(a_station.measure_id, dt=datetime.timedelta(days=2))[1]
    poly_tuple = polyfit(dates, levels, 3)
    poly = poly_tuple[0]
    date_offset = poly_tuple[1]

    assert type(poly) == numpy.poly1d
    assert poly.order == 3
    assert date_offset == datetime.date.today - dates[0]
