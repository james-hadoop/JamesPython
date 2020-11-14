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
                "header": ["SQL采集日期", "SQL范围", "SQL总数", "TDW转Hive成功数", "TDW转Hive成功率", "Hive语法验证成功数", "Hive语法验证成功率",
                           "Hive执行成功数",
                           "Hive执行成功率", "总体成功率"],
                "data1": ["2020-08-13", "所有SQL", "3533", "3487", "98.7%", "3431", "98.4%", "3032", "88.4%", "85.8%"],
                "data2": ["2020-08-13", "数据集市表", "49", "49", "100.0%", "48", "98.0%", "44", "91.7%", "89.8%"]
            }
        }
    }

    requests.post(url='http://10.100.73.235:23245/send_message', data={'data': json.dumps(data)})


def send_wechat_funnel():
    table = [
        ["SQL总数", 21510, 1, 89, 1],
        ["TDW转Hive", 21448, 0.9971, 89, 1],
        ["Hive语法验证", 21130, 0.9823, 87, 0.9775],
        ["Hive执行成功", 19863, 0.9234, 84, 0.9438]
    ]

    header = ['SQL转换漏斗', '所有SQL数', '所有SQL占比', '集市表SQL数', '集市表SQL占比']

    data = {
        'message_type': 'smart_table',
        'group_type': 'group',
        'id_list': ['19680206229'],
        'detail_params': {
            'isTable': {
                'title': '字段血缘关系解析覆盖度漏斗 - 20200826',
                'header': header,
                'data': table,
                'color_type': 'system',
                'color_columns': [2, 4, 6, 8],
                'color_sys_type': 'RED_NEG',
                'data_format': ['TXT', 'NOR', 'PER', 'NOR', 'PER']
            }
        }
    }

    requests.post(url='http://10.100.73.235:23245/send_message', data={'data': json.dumps(data)})


def send_wechat_funnel_of_data_assert():
    table = [
        ["数据资产非空字段", 2679, 1],
        ["血缘关系覆盖字段", 1863, 0.6954]
    ]

    header = ['数据明目', '数量', '占比']

    data = {
        'message_type': 'smart_table',
        'group_type': 'group',
        'id_list': ['19680206229'],
        'detail_params': {
            'isTable': {
                'title': '字段血缘关系解析覆盖度漏斗',
                'header': header,
                'data': table,
                'color_type': 'system',
                'color_columns': [2, 4, 6, 8],
                'color_sys_type': 'RED_NEG',
                'data_format': ['TXT', 'NOR', 'PER', 'NOR', 'PER']
            }
        }
    }

    requests.post(url='http://10.100.73.235:23245/send_message', data={'data': json.dumps(data)})


def main():
    # send_wechat_statistic()
    # send_wechat_funnel()
    send_wechat_funnel_of_data_assert()

if __name__ == '__main__':
    main()
    sys.exit(0)
