import pandas as pd
import numpy as np
import sys

from geopy.geocoders import Nominatim


def get_location_by_lat_lon(lat_lon):
    geolocator = Nominatim(user_agent="zcsd-application")
    location = geolocator.reverse(lat_lon)

    return str(location)


def main():
    geolocator = Nominatim(user_agent="zcsd-application")

    city = ["上海", "深圳"]
    # lat_lon = ["22.54173469543457, 113.9674606323242", "22.545774459838867, 113.92662048339844"]
    # lat_lon = ["22.541, 113.967", "22.545, 113.926"]
    # lat_lon = ["31.2, 121.4", "31.1, 121.4"]
    # lat_lon = ["31.2120, 121.5458", "31.2235, 121.4559"]
    lat_lon = ["31.212, 121.545", "31.223, 121.455"]
    lat_lon = ["31.129118, 121.37017", "31.2374, 121.4946"]


    arr = {"city": city,
           "lat_lon_str": lat_lon}

    log_df = pd.DataFrame(arr)
    print(log_df)

    print('-' * 120)

    log_df['behavior_location'] = log_df['lat_lon_str'].map(
        lambda x: "_NULL" if x == "nan, nan" else geolocator.reverse(x))

    print(log_df.head(5))


if __name__ == '__main__':
    pd.set_option('display.max_columns', 1000)

    pd.set_option('display.width', 1000)

    pd.set_option('display.max_colwidth', 1000)

    pd.set_option('display.max_rows', None)

    main()
    sys.exit(0)
