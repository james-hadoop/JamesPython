from geopy.geocoders import Nominatim

geolocator = Nominatim()


# update t_dwa_zcsd_user_log_summary set location='华翔路, 闵行区, 上海市, 201106, China 中国' where lat_str like '%31.2%'and lon_str like '%121.3%';
# update t_dwa_zcsd_user_log_summary set location='虹桥路, 虹景家苑, 长宁区, 上海市, 200336, China 中国' where lat_str like '%31.2%'and lon_str like '%121.4%';
# update t_dwa_zcsd_user_log_summary set location='雪野路, 浦东新区, 上海市, 200126, China 中国' where lat_str like '%31.2%'and lon_str like '%121.5%';
# update t_dwa_zcsd_user_log_summary set location='王桥, 川沙新镇, 浦东新区, 上海市, 201200, China 中国' where lat_str like '%31.2%'and lon_str like '%121.7%';
# update t_dwa_zcsd_user_log_summary set location='南大路, 大场镇, 上海市, 200436, China 中国' where lat_str like '%31.3%'and lon_str like '%121.4%';
# # 万祥镇, 浦东新区, 上海市, 201300, China 中国
# location = geolocator.reverse("31.000000, 121.800000")
# # 银都路, 曹行, 闵行区, 上海市, 201100, China 中国
# location = geolocator.reverse("31.100000, 121.400000")
# # 华翔路, 闵行区, 上海市, 201106, China 中国
# location = geolocator.reverse("31.200000, 121.300000")
# # 虹桥路, 虹景家苑, 长宁区, 上海市, 200336, China 中国
# location = geolocator.reverse("31.200000, 121.400000")
# 雪野路, 浦东新区, 上海市, 200126, China 中国
# location = geolocator.reverse("31.200000, 121.500000")
# # 王桥, 川沙新镇, 浦东新区, 上海市, 201200, China 中国
# location = geolocator.reverse("31.200000, 121.700000")
# 南大路, 大场镇, 上海市, 200436, China 中国
location = geolocator.reverse("31.300000, 121.400000")


print(location)

