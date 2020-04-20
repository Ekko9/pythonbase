import time, datetime
import cx_Oracle
import pandas as pd


def get_file(filepath1):
    # sql文件夹路径
    sql_path = 'path' + '\\'
    # sql文件名， .sql后缀的
    sql_file = 'SQL_File.sql'
    # 读取 sql 文件文本内容
    sql = open(sql_path + sql_file, 'r', encoding='utf8')
    sqltxt = sql.readlines()
    # 此时 sqltxt 为 list 类型
    # 读取之后关闭文件
    sql.close()
    # list 转 str
    sql = "".join(sqltxt)
    conn = cx_Oracle.connect('user', 'pwd', 'ip:1521/DB')
    today = datetime.date.today()
    yesterday = today + datetime.timedelta(days=-1)
    df = pd.read_sql(sql.format(yesterday), conn)
    df.to_excel(filepath1)
    conn.close()

