import base64
import re

# expression = 'J2tkJw=='
# clean_expression = re.sub('[\s+]', '', expression)
#
# bb = base64.decodebytes(clean_expression.encode())
# print(bb.decode("utf-8"))

# str = 'sng_mediaaccount_app.kandian_video_medium_full_info_d.kddaily_expose'
# src_table_name = str.rsplit('.', 1)[0]
# print(f"src_table_name={src_table_name}")

list_str=["0", "\tapplication_1589888927865_11666447:\nStage 0 succeeded:\n  Number of bytes read:          30026\n  Number of input records:       1318\n  Number of bytes written:       0\n  Number of output records:      0\n  Number of complete tasks:      1\n  Number of failed tasks:        0\n  Number of shuffle bytes read:  0\n  Number of shuffle record read: 0\n  Number of shuffle bytes write: 20\n  Number of shuffle record write:1\n  Total run time:                1798\n\tapplication_1589888927865_11666447:\nStage 1 succeeded:\n  Number of bytes read:          0\n  Number of input records:       0\n  Number of bytes written:       0\n  Number of output records:      1\n  Number of complete tasks:      1\n  Number of failed tasks:        0\n  Number of shuffle bytes read:  20\n  Number of shuffle record read: 1\n  Number of shuffle bytes write: 0\n  Number of shuffle record write:0\n  Total run time:                19809\n"]

print(list_str)
print(list_str[0])



