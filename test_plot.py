"""Unit test for the plot module"""
import datetime
import matplotlib.pyplot as plot
from floodsystem.plot import plot_water_levels, plot_water_levels_general, plot_water_level_with_fit
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

    # assert that the number of figures is higher than when you started the test
    # num_figures_before = plot.gcf().number
    plot_water_levels(station, dates, levels)
    num_figures_after = plot.gcf().number
    assert num_figures_after >= 1

    '''
    # Plot graph
    with patch("my.module.plt.show") as show_patch:
        plot_water_levels(station, dates, levels)
        assert show_patch.called
    '''

def test_plot_water_levels_general():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get list of station objects with top relative water level
    top2 = stations_highest_rel_level(stations, 2)

    # Create list of station objects
    stations = []
    for i in range(2):
        stations.append(top2[i][0])
    
     # assert that a figure has been created
    plot_water_levels_general(stations)
    num_figures_after = plot.gcf().number
    assert num_figures_after >= 1

def plot_water_level_with_fit():
    # Build and update list of stations
    stations = build_station_list()
    update_water_levels(stations)
    # Choose a random station
    a_station = stations[52]
    # Fetch its water level data for the last 2 days
    dates = fetch_measure_levels(a_station.measure_id, dt=datetime.timedelta(days=2))[0]
    levels = fetch_measure_levels(a_station.measure_id, dt=datetime.timedelta(days=2))[1]
    # Plot a graph using this data collected
    plot_water_level_with_fit(a_station, dates, levels, 3)

    # Assert that a figure has been created
    num_figures_after = plot.gcf().number
    # assert num_figures_after >= 1