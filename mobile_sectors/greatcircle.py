def location_at_distance(start_lon, start_lat, direction, distance=5):
    '''
    The purpose of this is to find a latitude and longitude at a specific distance from 
    another point. The inputs are the starting latitude and longitude, and the distance
    and angle to proceed from that point.
    
    http://www.edwilliams.org/avform147.htm#LL
    
    Inputs:
    - start_lat: metric degrees
    - start_lon: metric degrees
    - distance:  metres
    - direction: metric degrees
    '''
    from math import cos, sin, asin, pi

    radians = (pi/180) # multiply by degrees to get radians
    nm = 1/(60*1860)   # multiply by metres to get nautical miles

    start_lat = start_lat * radians
    start_lon = start_lon * radians
    distance = distance * nm * radians
    direction = direction * radians
    
    end_lat=asin(sin(start_lat)*cos(distance)+cos(start_lat)*sin(distance)*cos(direction))
    if (cos(end_lat)==0):
        end_lon=start_lon      # endpoint a pole
    else:
        end_lon=((start_lon-asin(sin(direction)*sin(distance)/cos(end_lat))+pi)%(2*pi))-pi
        
    return end_lat/radians, end_lon/radians

def test():
    import pandas as pd

    # Different distances in three bearings from a point near Cape Town.
    sites = [
        [18.565784, -33.603048, 0, 5],
        [18.565784, -33.603048, 120, 50],
        [18.565784, -33.603048, 240, 500],
    ]

    df = pd.DataFrame(sites, columns=['long', 'lat', 'azimuth', 'distance'])

    applied_df = \
        df.apply(lambda x: location_at_distance(x.long, x.lat, x.azimuth), axis='columns', result_type='expand') \
            .rename(columns={0: 'new_long', 1: 'new_lat'})
    df = pd.concat([df, applied_df], axis='columns')

    return df

if __name__ == '__main__':
    test()