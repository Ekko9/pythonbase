import cx_Oracle


# 连接数据库
def get_db_connection():

    conn = cx_Oracle.connect('user', 'pwd', 'ip:1521/DB')

    print('DB connection successful')
    return conn



