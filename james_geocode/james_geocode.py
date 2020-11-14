import sys

from geopy.geocoders import Nominatim


def get_location_by_lat_lon(lat_lon):
    geolocator = Nominatim(user_agent="zcsd-application")
    location = geolocator.reverse(lat_lon)

    return str(location)


def main():
    print(get_location_by_lat_lon("26.6054, 106.6435"))


if __name__ == '__main__':
    main()
    sys.exit(0)


