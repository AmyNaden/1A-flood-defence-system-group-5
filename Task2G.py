from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    update_water_levels(stations)

    severe_risk_towns = stations_level_over_threshold(stations, 2)
    high_risk_towns = stations_level_over_threshold(stations, 1.5)
    high_risk_towns.remove(severe_risk_towns)
    moderate_risk_towns = stations_level_over_threshold(stations, 1)
    moderate_risk_towns.remove(severe_risk_towns, high_risk_towns)
    low_risk_towns = []
    for i in range(len(stations)):
        
    severe_statement = "The towns at severe risk are: "
    for stations in severe_risk_towns:
        severe_statement += "{}, ".format(severe_risk_towns[i][0].name)        
    print(severe_statement)

    high_statement = "The towns at high risk are: "
    for i in range(len(high_risk_towns)):
        high_statement += "{}, ".format(high_risk_towns[i].name)
    print(high_statement)

    moderate_statement = "The towns at moderate risk are: "
    for i in range(len(moderate_risk_towns)):
        moderate_statement += "{}, ".format(moderate_risk_towns[i].name)
    print(moderate_statement)


        


