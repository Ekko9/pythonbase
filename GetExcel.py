import pandas as pd
import time,datetime
from ConnDB import get_db_connection


# 生成Excel
def get_excel(filepath):

    today = datetime.date.today()
    yesterday = today + datetime.timedelta(days=-1)

    sql = '''
    SELECT COUNT(*) 
    FROM B2C_USER 
    WHERE USERFROM <> '5' 
    AND USERTYPE = '1' 
    AND ACCOUNTYPE = '1' 
    AND TO_CHAR(REGTIME, 'YYYY-MM-DD') ='{0}'
    '''
    conn = get_db_connection()

# 直接使用pandas的read_sql即可转化成DataFrame
    df = pd.read_sql(sql.format(yesterday), conn)

    df.to_excel(filepath)

    print('Excel generated')
    conn.close()
    print('DB connection closed')

