import smtplib
import os
import time,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail():
    # Sender email
    fromaddr = 'XXXXX@sina.com'
    # Sender email pwd
    password = 'pwd'
    # Recipient email
    toaddrs = ['XXXXX@163.com']
    content = 'hello, this is SC_B2C网站(新版)数据统计.'
    textApart = MIMEText(content)
    today = datetime.date.today()
    yesterday = today + datetime.timedelta(days=-1)
    # 文件路径及文件
    a, b = os.path.split("path/Register_{0}.xlsx")
    excel_Register = a + "/" + b.format(yesterday)
    excel_Register_Apart = MIMEApplication(open(excel_Register, 'rb').read())
    excel_Register_Apart.add_header('Content-Disposition', 'attachment', filename=b.format(yesterday))
    # 文件路径及文件
    x, y = os.path.split("path/Count_{0}.xlsx")
    excel_Count = a + "/" + y.format(yesterday)
    excel_Count_Apart = MIMEApplication(open(excel_Count, 'rb').read())
    excel_Count_Apart.add_header('Content-Disposition', 'attachment', filename=y.format(yesterday))
    # 定义Title
    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(excel_Register_Apart)
    m.attach(excel_Count_Apart)
    m['Subject'] = 'SC_B2C Data Statistics'
    try:
        server = smtplib.SMTP()
        server.connect('smtp.sina.com', 25)
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('Email send success')
        server.quit()
    except smtplib.SMTPException as e:
        # 打印错误
        print('error:', e)



