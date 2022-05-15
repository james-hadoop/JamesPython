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
    print(f"{province}")
    print(f"{country}{province}{city}{district}")


def main():
    # 上海
    lat_lon = "31.225696563611,121.49884033194"
    # 香港
    lat_lon = "22.3566,114.0208"
    # 广西
    lat_lon = "25.8,109.58"
    # 台湾
    lat_lon = "25.05,121.50"
    # 西藏
    lat_lon = "29.97,91.11"
    # 新疆
    lat_lon = "43.45,87.36"
    # 内蒙古
    lat_lon = "40.83,111.73"

    parse_location_with_baidu_api(lat_lon)


if __name__ == "__main__":
    main()
