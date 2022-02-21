import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def plot_water_levels(station, dates, levels):
    '''Required for task 2E - displays a plot of water level data against time for a station'''
    # Plot main graph
    plt.plot(dates, levels, "-b", label="last 10 days")

    # Include plot lines for the typical low and high levels
    low_level = []
    high_level = []
    for i in range(len(dates)):
        low_level.append(station.typical_range[0])
        high_level.append(station.typical_range[1])
    plt.plot(dates, low_level, "-g", label="typical low")
    plt.plot(dates, high_level, "-r", label="typical high")
    
    # Axes should be labelled and use the station name as the plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Include key for each line
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
    

def plot_water_levels_general(stations):
    '''Extension task - Generalise plot to take a list of up to 6 stations and display the level at each station as single plot'''
    station_names = []
    # Loop through list of stations
    for i in range(len(stations)):
        station_names.append(stations[i].name)
        dt = 10
        dates, levels = fetch_measure_levels(stations[i].measure_id,
                                     dt=datetime.timedelta(days=dt))
        # Plot each graph as subgraph on single grap
        plt.plot(dates, levels, label=stations[i].name)
    
    # Axes should be labelled and use the station name as the plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station_names)

    # Include key for each line
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
