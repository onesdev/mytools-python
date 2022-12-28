"""
本程序主要用于获取IP地址并发送到指定邮箱
用法：使用windows计划任务设置开机用户登录后执行该脚本
"""

import socket
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

gateway = '192.168.31.1'  # 这里可以配置内网网关，或者某个内网服务器IP

smtp_host = 'smtp.qq.com'
smtp_port = 25  # 默认SMTP协议端口为25
mail_user = '20761927@qq.com'
mail_pass = 'inhqkkbidweacabi'  # 你的邮箱密码


def get_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect((gateway, 1))
        ip = st.getsockname()[0]
    except Exception:
        ip = ''
    finally:
        st.close()
    return ip

def send_email(ip):
    message = MIMEText('当前主机IP地址为：' + ip, 'plain', 'utf-8')
    message['From'] = Header(mail_user, 'utf-8')
    message['to'] = Header(mail_user, 'utf-8')
    message['Subject'] = Header('您的主机IP地址', 'utf-8')

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(smtp_host, smtp_port)
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(mail_user, mail_user, message.as_string())
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
    finally:
        smtp_obj.quit()


if __name__ == '__main__':
    # 先休眠3分钟，等内网安全助手登录认证后获取内网IP
    time.sleep(180)
    ip = get_ip()
    # 可能出现内网安全助手认证超时的情况，此时ip地址是''，等待60秒后再次尝试获取
    while ip == '':
        time.sleep(60)
        ip = get_ip()
    send_email(ip)

    # 每隔1个小时获取一次IP地址，与老地址比对，如果有变化，就重新发送邮件
    while 1:
        time.sleep(3600)
        new_ip = get_ip()
        if new_ip != '' and new_ip != ip:
            ip = new_ip
            send_email(ip)

