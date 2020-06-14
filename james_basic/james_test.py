import base64
import re

expression = 'J2tkJw=='
clean_expression = re.sub('[\s+]', '', expression)

bb = base64.decodebytes(clean_expression.encode())
print(bb.decode("utf-8"))

# str = 'sng_mediaaccount_app.kandian_video_medium_full_info_d.kddaily_expose'
# src_table_name = str.rsplit('.', 1)[0]
# print(f"src_table_name={src_table_name}")
