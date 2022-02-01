from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations



def run1():
    """Requirements for Task 1D part 1"""

    # Build list of stations
    stations = build_station_list()

    # Print how many rivers have at least one monitoring station 
    rivers = rivers_with_station(stations)
    print(str(len(rivers))+' stations.')
    
    # Print the first 10 rivers in alphebetical order
    rivers.sort()
    print('First 10 - '+rivers[:10])


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run1()