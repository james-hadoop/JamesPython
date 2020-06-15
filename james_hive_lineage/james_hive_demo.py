from pyhive import hive

conn = hive.Connection(host='localhost', port=10000, username='', database='sng_mediaaccount_app')

cursor = conn.cursor()
cursor.execute('SHOW TABLES')
# 打印结果
for result in cursor.fetchall():
    print(result)
