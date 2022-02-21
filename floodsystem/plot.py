import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    '''Required for task 2E - displays a plot of water level data against time for a station'''
    # Plot
    plt.plot(dates, levels)
    # Include plot lines for the typical low and high levels
    
    # Axes should be labelled and use the station name as the plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
