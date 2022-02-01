from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import station_names 


def run1():
    """Requirements for Task 1D part 1"""

    # Build list of stations
    stations = build_station_list()

    # Print how many rivers have at least one monitoring station 
    rivers = rivers_with_station(stations)
    print(str(len(rivers))+' stations.')
    
    # Print the first 10 rivers in alphebetical order
    rivers_sorted = sorted(rivers)
    print('First 10 - '+str(rivers_sorted[:10]))


def run2():
    '''Requirements for Task 1D part 2'''
    # Build list of stations
    stations = build_station_list()

    # Gererate dictionary with river name as the key 
    rivers_dict = stations_by_river(stations) 

    # Print names of stations on the River Aire
    aire_stations = rivers_dict['River Aire']
    print('\nStations on the River Aire - ', station_names(aire_stations))

    # Print names of stations on the River Cam
    cam_stations = rivers_dict['River Cam']
    print('\nStations on the River Cam - ', station_names(cam_stations))

    # Print names of stations on the River Thames
    thames_stations = rivers_dict['River Thames']
    print('\nStations on the River Thames - ', station_names(thames_stations))


if __name__ == "__main__":
    print("*** Task 1D Part 1: CUED Part IA Flood Warning System ***")
    run1()
    print()
    print("*** Task 1D Part 2: CUED Part IA Flood Warning System ***")
    run2()