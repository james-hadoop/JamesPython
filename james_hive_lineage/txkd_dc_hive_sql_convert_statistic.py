# coding:utf-8
import datetime
import sys
import requests
import json


def send_wechat_statistic():
    data = {
        'message_type': 'table',
        'group_type': 'group',
        'id_list': ['19680206229'],
        'detail_params': {
            'isTable': {
                "header": ["SQL采集日期","SQL范围", "SQL总数", "TDW转Hive成功数", "TDW转Hive成功率", "Hive语法验证成功数", "Hive语法验证成功率", "Hive执行成功数",
                           "Hive执行成功率", "总体成功率"],
                "data1": ["2020-08-13", "所有SQL", "3533", "3487", "98.7%", "3431", "98.4%", "3032", "88.4%", "85.8%"],
                "data2": ["2020-08-13", "数据集市表", "49", "49", "100.0%", "48", "98.0%", "44", "91.7%", "89.8%"]
            }
        }
    }

    requests.post(url='http://10.100.73.235:23245/send_message', data={'data': json.dumps(data)})


def main():
    send_wechat_statistic()


if __name__ == '__main__':
    main()
    sys.exit(0)
