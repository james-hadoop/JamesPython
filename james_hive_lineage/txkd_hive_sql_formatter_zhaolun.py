#-*- coding:utf-8 -*-

import datetime
import re
import sys
from importlib import reload

reload(sys) 
sys.setdefaultencoding('utf8') 
import json
import os
import re
import base64
import sqlparse
import itertools
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML
import hashlib


def is_subselect(parsed):
    if not parsed.is_group:
        return False
    for item in parsed.tokens:
        if item.ttype is DML and item.value.upper() == 'SELECT':
            return True
    return False


def extract_from_part(parsed):
    from_seen = False
    for item in parsed.tokens:
        #print item
        if item.is_group:
            for x in extract_from_part(item):
                yield x
        if from_seen:
            if is_subselect(item):
                for x in extract_from_part(item):
                    yield x
            elif item.ttype is Keyword and item.value.upper() in ['ORDER', 'GROUP', 'BY', 'HAVING', 'GROUP BY']:
                from_seen = False
                StopIteration
            else:
                yield item
        if item.ttype is Keyword and item.value.upper()=='FROM':
            from_seen = True


def extract_table_identifiers(token_stream):
    for item in token_stream:
        if isinstance(item, IdentifierList):
            for identifier in item.get_identifiers():
                value = identifier.value.replace('"', '').lower()                
                yield value
        elif isinstance(item, Identifier):
            value = item.value.replace('"', '').lower()
            yield value


def extract_tables(sql):
    # let's handle multiple statements in one sql string
    extracted_tables = []
    statements = list(sqlparse.parse(sql))
    for statement in statements:
        if statement.get_type() != 'UNKNOWN':
            stream = extract_from_part(statement)
            extracted_tables.append(set(list(extract_table_identifiers(stream))))
    return list(itertools.chain(*extracted_tables))

def dfs_extract_tables(sql):
    sql = sql.strip()
    list_sub_sql = []
    list_sub_sql.append(sql)
    table_set = set()

    rs = re.findall(r'insert\s+into\s+table\s+([\.\:\w]+)', sql, flags=(re.MULTILINE|re.IGNORECASE))
    if rs is not None:
        for t in rs:
            table_set.add(t)
    while len(list_sub_sql) > 0:
        sql0 = list_sub_sql.pop()
        new_sub_sqls = extract_tables(sql0)
        for sql in new_sub_sqls:
            idx1,idx2 = sql.find('('),sql.rfind(')')
            if(idx1 < idx2):
                list_sub_sql.append(sql[idx1+1:idx2 - idx1])
            else:
                table_set.add(sql)
    #print "\n".join(table_set)
    return ",".join(table_set)






#------------------------------
# 为unbase64()函数强转String
def convert_unbase64(sql):
    rs = re.findall(r'''[^a-zA-Z](unbase64\s*\([^()]*?\))''', sql, flags=re.IGNORECASE)
    if rs is not None:
        for t in rs:
            sql = sql.replace(t, 'cast(%s as string)' % t)
    return sql

# 为date_sub()函数增加单引号
def add_quote_on_date_for_DATE_SUB(sql):
    rs = re.findall(r'''date_sub(\(\s*([0-9]{8})\s*\,)''', sql, flags=re.IGNORECASE)
    if rs is not None:
        for t in rs:
            sql = sql.replace(t[0], t[0].replace(t[1], "'%s'" % t[1]))
    return sql


# 为date_add()函数增加单引号
def add_quote_on_date_for_DATE_ADD(sql):
    rs = re.findall(r'''date_add(\(\s*([0-9]{8})\s*\,)''', sql, flags=re.IGNORECASE)
    if rs is not None:
        for t in rs:
            sql = sql.replace(t[0], t[0].replace(t[1], "'%s'" % t[1]))
    return sql


# 常量替换
def replaceConstant(sql):
    pre_sql = sql.replace("TOK_SINGLE_QUOTE", "'")\
        .replace("TOK_BACKSLASH_N", "\n")\
        .replace("interval", "`interval`")\
        .replace('::','.')\
        .replace('\t',' ')
    return pre_sql
def replaceKey(pre_sql, key):
    rs = re.findall('[^a-zA-z](%s)[^a-zA-z]' % key, pre_sql, flags=re.IGNORECASE)
    rep_list = []
    if rs is not None:
        for t in rs:
            if t not in rep_list:
                rep_list.add(t)
        for t in rep_list:
            pre_sql = pre_sql.replace(t, '`%s`' % t)
    return pre_sql.rep_list('``%s``' % t, '`%s`' % t)

# insert table替换
def replaceInsert(pre_sql):
    pre_sql = re.sub(r'INSERT\s+TABLE','INSERT INTO TABLE', pre_sql, flags=re.IGNORECASE)
    pre_sql = re.sub(r'INSERT\s+OVERWRITE\s+INTO\s+TABLE','INSERT INTO TABLE', pre_sql, flags=re.IGNORECASE)
    pre_sql = re.sub(r'INSERT\s+OVERWRITE\s+TABLE','INSERT INTO TABLE', pre_sql, flags=re.IGNORECASE)
    pre_sql = re.sub(r'INSERT\s+INTO\s+TABLE','INSERT INTO TABLE', pre_sql, flags=re.IGNORECASE)
    
    #去掉多余空格
    pre_sql = re.subn(r'\s{2,}',' ', pre_sql)
    return pre_sql[0]


def sql2mysql(sql):
    return sql.replace("'", "TOK_SINGLE_QUOTE").replace("\n", "TOK_BACKSLASH_N")


# 为join或group缺少的别名加上别名
def solve_less_alias_problem(pre_sql):
    rs = re.findall(r'''(\)\s*\))\s+\w+?\s+on''', pre_sql, flags=re.IGNORECASE)
    if rs is not None:
        for t in rs:
            pre_sql = pre_sql.replace(t, ') t_alias_tt) ')
    rs = re.subn(r'\)\s*GROUP\s+BY', ') t_alias_tt GROUP BY', pre_sql, flags=re.IGNORECASE)
    pre_sql = rs[0]
    #print '--------------------------------'
    #print "group by replace %s times" % rs[1]
    #print rs[1]
    pre_sql = re.subn(r'\)\s*WHERE\s+',') t_alias_tt WHERE', pre_sql, flags=re.IGNORECASE)[0]

    rs = re.findall(r'((\sin\s*\([^()]*?\))\s*t_alias_tt)', pre_sql, flags=re.IGNORECASE)
    #print '--------------------------------'
    #print "####################RS -> ",rs
    if rs is not None:
        for t in rs:
            pre_sql = pre_sql.replace(t[0], t[1])

    return pre_sql


# 删除partion子句
def remove_partition_part(sql):
    sql = re.sub(r"(?i)(partition\s*\(\s*\w*\s*=\s*\w*\s*\))", " ", sql,flags=re.IGNORECASE)
    return sql


def replaceUDF(sql):
    sql = sql.replace('@pyspark ','')
    #替换常用udf 
    sql = re.subn(r"""parse_article_union_chann\s*\(\s*union_chann\s*,\s*\'2\.0\.0\'\s*\)""", "union_chann", sql,flags=re.IGNORECASE)[0]
    return sql



flag_replace = False

def bfs_analyse_sql(item,list_value,with_map):
    global flag_replace
    if item.is_keyword:
        list_value.append(item.value)
        if item.value.upper() in ('FROM','JOIN') or item.value.upper().endswith(' JOIN'):
            flag_replace = True
        elif item.value.upper() == 'SELECT':
            flag_replace = False
    elif item.is_group:
        if len(item.tokens) == 3 and with_map.has_key(item[0].value) and flag_replace == True:
            flag_replace = False
            #print 'bfs_analyse_sql-listvalue',list_value
            list_value.append(with_map[item[0].value])
            list_value.append(item[1].value)
            list_value.append(item[2].value)
        else:
            for x in item.tokens:
                bfs_analyse_sql(x,list_value,with_map)
    else:
        if with_map.has_key(item.value) and flag_replace:
            list_value.append(with_map[item.value])

        list_value.append(item.value)

def revertWith(sql,with_map = {},pass_to_sec_check = False):
    global flag_replace
    flag_replace = False
    sql = sql.strip()
    statements = list(sqlparse.parse(sql))
    for statement in statements:
        if statement.get_type() == 'UNKNOWN':
            print "UNKNOWN"
            return None
        #new_list = [x for x in statement.tokens if x.is_whitespace == False]
        it = iter(statement)
        flag_find_with = False
        #with_map = {}
        list_value = []
        while True:
            try:
                if pass_to_sec_check:
                    #print 'sub_sql direct to sec check..',sql
                    break
                x = next(it)
                if x.is_keyword and x.value.upper() == 'WITH':
                    flag_find_with = True
                    continue
                if x.is_keyword and x.value.upper() == 'SELECT':
                    flag_find_with = False
                    list_value.append(x.value)
                elif flag_find_with and x.is_group:
                    for y in x.tokens:
                        if y.is_group :
                            with_table_name = None
                            flag_before_as = True
                            for z in y.tokens:
                                if z.is_whitespace == False:
                                    if flag_before_as and z.is_keyword == False and z.value.upper() != 'AS':
                                        with_table_name = z.value
                                        continue
                                    if flag_before_as and z.is_keyword == True and z.value.upper() == 'AS':
                                        flag_before_as = False
                                        continue
                                    if flag_before_as == False and  (z.is_keyword == False or z.is_group):
                                        if(with_table_name is not None):
                                            tmp_z_value = z.value.strip()
                                            #print '----------------------------------------------------------------------------------------'
                                            #print 'tmp_z_value ->',tmp_z_value
                                            idx1,idx2 = tmp_z_value.find('('),tmp_z_value.rfind(')')
                                            if z.is_group and  tmp_z_value.startswith('(') :
                                                sub_sql_tmp = tmp_z_value[idx1+1:idx2 - idx1]
                                                ##print '!!!sub_sql_tmp -> ',sub_sql_tmp
                                                new_sub_sql = revertWith(sub_sql_tmp, with_map, True)
                                                with_map[with_table_name.lower()] = "(%s)" % new_sub_sql
                                                ##print '#####repalce update map => key:%s,map:%s'% (with_table_name.lower(),new_sub_sql)
                                            else:
                                                with_map[with_table_name.lower()] = z.value
                                                ##print '&&&&&nomal update map => key:%s,map:%s'% (with_table_name.lower(),z.value)
                                            #print with_map
                    #for循环结束，with_map读取完，跳出循环
                    break
                else:
                    list_value.append(x.value)
            except StopIteration:
                break
        while True:
            try:
                item = next(it)
                #if item.is_whitespace == False:
                #    print "## sec loop:",item.value
                bfs_analyse_sql(item,list_value,with_map)
            except StopIteration:
                break
        # print "list_value -> ",list_value
        return "".join(list_value)





def create_validate_sql(sql):
    #0.替换常量 保证sqlparse识别
    sql = replaceConstant(sql)
    #1 干掉insert ....values 不处理
    rs = re.findall(r'INSERT\s+INTO\s+.*?VALUES\s*\(',sql,flags=(re.MULTILINE|re.IGNORECASE))
    if(rs is not None and len(rs) > 0):
        print "pass",rs
        return None
    #2.sqlparse干掉sql中的注释
    sql = sqlparse.format(sql, reindent=True, strip_comments=True)
    #3.替换换行和多余的空格
    sql = re.subn(r'\s{2,}',' ', sql.replace('\n',' '))[0]
    #5.为date_add()、date_sub()函数增加单引号
    sql = add_quote_on_date_for_DATE_SUB(sql)
    sql = add_quote_on_date_for_DATE_ADD(sql)
    #6. insert table替换
    sql = replaceInsert(sql)
    #7.删除partion子句, 删除overwrite子句
    sql = remove_partition_part(sql)
    #8.convert_unbase64
    sql = convert_unbase64(sql)
    #9. replaceUDF
    sql = replaceUDF(sql)
    #10. replaceKey
    #sql = replaceKey(sql,'type')
    #11.替换with
    sql = revertWith(sql)
    #print sql
    #12.为join缺少的别名加上别名
    print type(sql)
    sql = solve_less_alias_problem(sql)
    #print '-' * 100
    #13, 套一层select * from ( )xx 
    #print sql
    idx = sql.lower().find('select ')
    if idx != -1:
        sql = sql[:idx] + 'select * from (' + sql[idx:] + ') xx'
        
    #print sql
    return sql




lines = open('txkd_dc_sql_60_big.txt').read().split('\n')
out_file = open('parsed_sql.txt','w')
pared_failed = open('parsed_fail_sql.txt','w')
cnt = 0;
for line in lines[:]:
    if line == "":
        continue
    arr = line.split("；")
    default_db = arr[1]
    sql = "；".join(arr[3:])
    origin_sql = sql 
    parsed_sql = None
    try:
        parsed_sql = create_validate_sql(sql)
    except:
        pass
    if(parsed_sql is not None):
        out_file.write((default_db + "；" 
             + parsed_sql + "；"
             + hashlib.sha1(parsed_sql).hexdigest() 
             + "；" + origin_sql + "；" 
             + hashlib.sha1(origin_sql).hexdigest() + "\n").encode('utf-8'))
    else:
        pared_failed.write(line)
        pared_failed.write("\n")
    cnt += 1
    print cnt 


out_file.close()
pared_failed.close()







