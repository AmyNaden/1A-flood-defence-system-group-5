from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np
import datetime

# Defining parameters for risk levels globally
global high, moderate, severe
high = 1
severe = 2
moderate = 1.5


def run():
    # Building station list and updating water levels
    stations = build_station_list()
    update_water_levels(stations)
    # This program will mainly use the current water level compared to its typical high level as an
    # indication factor of weather it will flood
    risk_levels = []
    for i in range(len(stations)):
        risk_level = stations[i].relative_water_level()
        risk_levels.append(risk_level)
    # Creating lists to fill with stations 
    severe_risk_towns = []
    high_risk_towns = []
    moderate_risk_towns = []
    low_risk_towns = []
    # Adding to lists dependent on risk level
    for i in range(len(risk_levels)):
        if risk_levels[i] != None:
            if risk_levels[i] > severe:
                severe_risk_towns.append(stations[i])
            elif high < risk_levels[i] < severe:
                high_risk_towns.append(stations[i])
            elif moderate < risk_levels[i] < high:
                moderate_risk_towns.append(stations[i])
            else:
                low_risk_towns.append(stations[i])

    # Defining a list to fill with towns where risk level is increasing
    water_level_increasing = []
    water_level_decreasing = []
    corrupt_stations = []
    for i in range(len(high_risk_towns)):
        # Fetching data for polyfit function to approximate function
        try:
            dates = fetch_measure_levels(high_risk_towns[i].measure_id, dt=datetime.timedelta(days=2))[0]
            levels = fetch_measure_levels(high_risk_towns[i].measure_id, dt=datetime.timedelta(days=2))[1]
        except:
            corrupt_stations.append(high_risk_towns[i].name)

        flag = True 
        if len(dates) == 0:
            flag = False
        for j in range(len(levels)):
            if type(levels[j]) != float:
                flag = False 
        if flag == True:
            poly_tuple = polyfit(dates, levels, 4)
            poly = poly_tuple[0]
            # Taking derivative
            derivative = np.polyder(poly, m=1)
            # Evaluating at the time now (list begins at most recent data)
            derivative_now = derivative(0)
            # If derivative greater than 0 then water level increasing!
            if derivative_now > 0:
                water_level_increasing.append(high_risk_towns[i])
            if derivative_now < 0:
                water_level_decreasing.append(high_risk_towns[i])
        else:
            corrupt_stations.append(high_risk_towns[i].name)

    print(corrupt_stations)
    # Setting condition to prevent an infinite loop
    choice = True           
    while choice == True:
        # Asking for user input to decide what list will be displayed
        print('\nPlease enter a valid risk level: severe, high, moderate or low, or press enter to quit program')
        option = str(input("What risk level would you like to see? "))
        if option == "severe":
            # Constructing statement of towns at severe risk            
            severe_statement = "----The towns at severe risk are: "
            # Constructing statement for decrease in water levels
            severe_changing_statement = "Phew- looks like the worst is behind these towns: "
            # Iterating through severe risk towns to ass them to the list
            for i in range(len(severe_risk_towns)):
                severe_statement += "{}, ".format(severe_risk_towns[i].name) 
                # Adding to list of towns that may soon be safe
                if severe_risk_towns[i] in water_level_decreasing:
                    severe_changing_statement += "{}".format(severe_risk_towns[i].name)
            # Printing list     
            print(severe_statement)

        # Repeating for other options
        elif option == "high":
            high_statement = "\n----The towns at high risk are: "
            high_changing_statement = "\n!!! THESE AREAS MAY SOON BE AT SEVERE RISK: "
            for i in range(len(high_risk_towns)):
                high_statement += "{}, ".format(high_risk_towns[i].name)
                if high_risk_towns[i] in water_level_increasing:
                    high_changing_statement += "{}, ".format(high_risk_towns[i].name)
            print(high_statement)
            print(high_changing_statement + "!!!")
            

        elif option == "moderate":
            moderate_statement = "\n----The towns at moderate risk are: "
            for i in range(len(moderate_risk_towns)):
                moderate_statement += "{}, ".format(moderate_risk_towns[i].name)
            print(moderate_statement)

        elif option == "low":
            low_statement = "\n----The towns at low risk are: "
            for i in range(len(low_risk_towns)):
                low_statement += "{}, ".format(low_risk_towns[i].name)
                if low_risk_towns[i] in water_level_increasing:
                    low_changing_statement += "{}, ".format(low_risk_towns[i].name)
            print(low_statement)
            print(low_changing_statement)
        # Allowing exit from loop
        elif option == '':
            choice = False
        # Allowing for possibility that user enters invalid responce
        else:
            print("This is not a valid response")

if __name__ == "__main__":
    print("\n*** Task 2G: CUED Part IA Flood Warning System ***")
    run()



