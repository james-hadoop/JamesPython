import pandas as pd
import os
import sys


def traverse_dir(dir_path):
    file_cnt = 0

    file_set = set()
    file_list = []
    file_dict = dict()

    for dir_path, dir_names, filenames in os.walk(dir_path):
        for filename in filenames:
            # print(dir_path)
            # print(filename)
            print(os.path.join(dir_path, filename))
            full_file_path = os.path.join(dir_path, filename)

            new_file_name = str(filename).replace(" ", "_").replace("《", "").replace("》", "").replace("｜", "_").replace(
                ":", "_").replace("：", "_").replace("/", "_")

            new_full_file_path = os.path.join(dir_path, new_file_name)
            os.rename(full_file_path, new_full_file_path)

            # 更新元素
            file_dict.update({new_full_file_path: new_file_name})
            file_list.append(new_file_name)
            file_set.add(new_file_name)

            file_cnt += 1

    print(f"file_cnt={file_cnt}")
    print("-" * 64)

    # for filename in file_list:
    #     print(filename)
    #

    # for key in file_dict.keys():
    #     print(f"{key} --> {file_dict.get(key)}")
    # print("-" * 64)
    #
    # file_list.sort()
    # for file_name in file_list:
    #     print(f"\t{file_name}")
    # print("-" * 64)

    file_items = file_dict.items()
    file_name_list = []
    for key, value in file_items:
        if value not in file_set:
            print(f"{key} --> {value}")


def main():
    traverse_dir("/Users/qian.jiang/Documents/_AllDocMap/04_eBook")


if __name__ == '__main__':
    pd.set_option('display.max_columns', 1000)

    pd.set_option('display.width', 1000)

    pd.set_option('display.max_colwidth', 1000)

    pd.set_option('display.max_rows', None)

    main()
    sys.exit(0)
