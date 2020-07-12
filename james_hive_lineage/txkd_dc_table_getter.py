import json


def composeDdl(db_name, table_name, columns):
    dbDdl = "create database if not exists " + db_name + "; use " + db_name + ";";
    tableDllPrefix = "CREATE TABLE if not exists " + table_name + "( "
    tableDdlPostfix = " );"

    return dbDdl + tableDllPrefix + columns + tableDdlPostfix


def makeDdl():
    ddlList = []
    table_tuple_list = parse_tdw_table()
    for tpl in table_tuple_list:
        print(tpl[0] + " - " + tpl[1] + " - " + tpl[2])
        dbName = tpl[0]
        tableName = tpl[1]
        tableOwner = tpl[2]
        col_list = tpl[3]
        cols = [str(item).replace("\'", "\"") for item in col_list]
        columns = ""
        for c in cols:
            # print(c)
            col_dict = json.loads(c)
            # print(f"colName={col_dict['colName']} - colType={col_dict['colType']} - colOrder={col_dict['order']}")
            colName = col_dict['colName']
            colType = col_dict['colType']
            columns = columns + colName + " " + colType + ","

        columns = columns[:len(columns) - 1]
        print(f"columns={columns}")
        ddlList.append(composeDdl(dbName, tableName, columns))

    return ddlList


def parse_tdw_table():
    with open('/Users/qjiang/workspace4py/JamesPython/james_hive_lineage/_data/数据集市表_4.json', 'r') as f:
        data = f.read()

        json_dict = json.loads(data)
        data_list = json_dict['data']['list']

        table_tuple_list = []
        table_info_list = [str(item).replace("\'", "\"").replace("None", "\"None\"").replace("False", "\"False\"") for item in data_list]
        for t in table_info_list:
            print(t)
            table_dict = json.loads(t)
            # print(
            #     f"databaseName={table_dict['databaseName']} - tableName={table_dict['tableName']} - owner={table_dict['owner']}")
            table_tuple_list.append(
                (table_dict['databaseName'], table_dict['tableName'], table_dict['owner'], table_dict['cols']))

    return table_tuple_list


def main():
    ddlList = makeDdl()
    print('-' * 160)

    with open("_data/ddl.sql", "a+") as f:
        for ddl in ddlList:
            print(ddl)
            f.write(ddl + "\n")


if __name__ == '__main__':
    main()
