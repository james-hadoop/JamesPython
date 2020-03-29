def fetch_all(COR, sql):  # wrapper for sql
    COR.execute(sql)
    return COR.fetchall()


def execute_sql(COR, CON, sql):
    COR.execute(sql)
    CON.commit()
