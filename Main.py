from GetExcel import get_excel
from Sql_File import get_file
from Send_Mail import send_mail
from DelFile import delete_file
import time,datetime
if __name__ == '__main__':
    # 获取昨天的时间
    today = datetime.date.today()
    yesterday = today + datetime.timedelta(days=-1)
    filepath = 'path/Register_{}.xlsx'.format(yesterday)
    filepath1 = 'path/Count_{}.xlsx'.format(yesterday)

delete_file()
get_file(filepath1)
get_excel(filepath)
send_mail()
