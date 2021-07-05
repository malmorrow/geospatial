def location_at_distance(start_lat, start_lon, distance, direction):
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