from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

def run():
    stations = build_station_list()
    update_water_levels(stations)
    risk_levels = []
    for i in range(len(stations)):
        risk_level = stations[i].relative_water_level()
        risk_levels.append(risk_level)
    severe_risk_towns = []
    high_risk_towns = []
    moderate_risk_towns = []
    low_risk_towns = []
    for i in range(len(risk_levels)):
        if risk_levels[i] != None:
            if risk_levels[i] > 2:
                severe_risk_towns.append(stations[i])
            elif 1.5 < risk_levels[i] < 2:
                high_risk_towns.append(stations[i])
            elif 1 < risk_levels[i] < 1.5:
                moderate_risk_towns.append(stations[i])
            else:
                low_risk_towns.append(stations[i])

    # Constructing statement of towns at severe risk            
    severe_statement = "----The towns at severe risk are: "
    # Iterating through severe risk towns to ass them to the list
    for i in range(len(severe_risk_towns)):
        severe_statement += "{}, ".format(severe_risk_towns[i].name)   
    # Printing list     
    print(severe_statement)

    high_statement = "----The towns at high risk are: "
    for i in range(len(high_risk_towns)):
        high_statement += "{}, ".format(high_risk_towns[i].name)
    print(high_statement)

    moderate_statement = "----The towns at moderate risk are: "
    for i in range(len(moderate_risk_towns)):
        moderate_statement += "{}, ".format(moderate_risk_towns[i].name)
    print(moderate_statement)

    low_statement = "----The towns at low risk are: "
    for i in range(len(low_risk_towns)):
        low_statement += "{}, ".format(low_risk_towns[i].name)
    print(low_statement)

if __name__ == "__main__":
    print("\n*** Task 2G: CUED Part IA Flood Warning System ***")
    run()



