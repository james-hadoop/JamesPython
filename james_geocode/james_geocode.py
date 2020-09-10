import sys

from geopy.geocoders import Nominatim


def get_location_by_lat_lon(lat_lon):
    geolocator = Nominatim(user_agent="zcsd-application")
    location = geolocator.reverse(lat_lon)

    print(location)


def main():
    get_location_by_lat_lon("22.5, 113.9")


if __name__ == '__main__':
    main()
    sys.exit(0)


