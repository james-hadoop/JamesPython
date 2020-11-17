import requests
import json


def parse_location_with_baidu_api(lat_lon):
    baidu_map_url_prefix = "http://api.map.baidu.com/reverse_geocoding/v3/?ak=t0cHujK5IFBwzt9IUsZkFgdHhCicOB15&output=json&coordtype=wgs84ll&location="

    req_url = f"{baidu_map_url_prefix}{lat_lon}"
    print(f"reqt_url={req_url}")

    resp_json = requests.get(req_url).json()
    print(resp_json.get("result").get("formatted_address"))

    country = resp_json.get("result").get("addressComponent").get("country")
    province = resp_json.get("result").get("addressComponent").get("province")
    city = resp_json.get("result").get("addressComponent").get("city")
    district = resp_json.get("result").get("addressComponent").get("district")
    print(f"{country}{province}{city}{district}")


def main():
    lat_lon = "31.225696563611,121.49884033194"
    parse_location_with_baidu_api(lat_lon)


if __name__ == "__main__":
    main()
