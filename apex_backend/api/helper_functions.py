# file for helper functions used throughout this project

import math as m 
import json

def get_second_delta(t1, t2):
    
    """
    Get seconds from hhmmss time string.
    """

    t1 = t1.split('.')[0]
    t2 = t2.split('.')[0]
    dt = int(t2) - int(t1)

    return dt

def haversine_formula(lat1, long1, lat2, long2):

    """ Calculate the distance between two lat/longs on a globe
    Reference here: https://www.movable-type.co.uk/scripts/latlong.html
    """

    R = 6371000

    phi1 = lat1 * m.pi/180
    phi2 = lat2 * m.pi/180 

    dphi = (lat2 - lat1) * m.pi/180
    dlam = (long2 - long1) * m.pi/180

    a = m.sin(dphi/2)**2 + m.cos(dphi)*m.cos(phi2)*(m.sin(dlam/2)**2)
    c = m.atan2(m.sqrt(a), m.sqrt(1-a))
    
    distance = R * c # distance in meters

    return(round(distance,3))


def apex_area_swept(rawdata_list):

    print('YOU MADE IT HERE')
    data = json.loads(rawdata_list)
    meters_traveled = 0
    total_time = 0

    for i in range(0, len(data) - 1):

        lat1 = float(data[i]['latitude'])
        lat2 = float(data[i+1]['latitude'])
        long1 = float(data[i]['longitude'])
        long2 = float(data[i+1]['longitude'])
        dt = get_second_delta(data[i]['gps_hhmmss'], data[i+1]['gps_hhmmss'])

        print('\nMETERS TRAVELLED: {}'.format(haversine_formula(lat1, long1, lat2, long2)))
        print('TIME DELTA: {} SECONDS'.format(dt))

        meters_traveled = meters_traveled + haversine_formula(lat1, long1, lat2, long2)
        total_time = total_time + dt

    return(meters_traveled, total_time)