def dist(lat1, long1, lat2, long2):
    '''
    Populate the geometric data using a CRS that understands latitudes and longitudes:
    epsg:4326
    Convert the data into an equal-distance CRS. This is a global equal-distance CRS:
    epsg:32663
    '''
    import geopandas as gpd
    from shapely.geometry import Point
    geom=[Point(xy) for xy in zip([long1,long2], [lat1,lat2])]
    gdf=gpd.GeoDataFrame(geometry=geom,crs={'init':'epsg:4326'})
    gdf.to_crs(epsg=32663,inplace=True)
    l=gdf.distance(gdf.shift())
    print(l)
