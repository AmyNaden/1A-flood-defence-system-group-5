"""Unit test for the plot module"""
import datetime
import patch
from floodsystem.plot import plot_water_levels, plot_water_levels_general
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.datafetcher import fetch_measure_levels



def test_plot_water_levels():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get list of station objects with top relative water level
    top_station = stations_highest_rel_level(stations, 1)

    # Get variable to plot 
    station = top_station[0][0]
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    # Plot graph
    with patch("my.module.plt.show") as show_patch:
        plot_water_levels(station, dates, levels)
        assert show_patch.called

def test_plot_water_levels_general():
    pass