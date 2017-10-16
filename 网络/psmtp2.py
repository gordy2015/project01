#!/usr/bin/python
#  coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from email.header import Header
import sys

# 设置默认字符集为UTF8 不然有些时候转码会出问题
default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)

# 发送邮件的相关信息，根据你实际情况填写
smtpHost = 'smtp.ruaaji.cn'
smtpPort = '25'
sslPort = '465'
fromMail = 'abc@ruaaji.cn'
toMail = 'abc@qq.com'
username = 'abc@ruaaji.cn'
password = '!8888'

# 邮件标题和内容
subject = u'[Notice]hello'
body = u'hello,this is a mail from 9 ' + fromMail

# 初始化邮件
encoding = 'utf-8'
mail = MIMEText(body.encode(encoding), 'plain', encoding)
mail['Subject'] = Header(subject, encoding)
mail['From'] = fromMail
mail['To'] = toMail
mail['Date'] = formatdate()

try:
    # 连接smtp服务器，明文/SSL/TLS三种方式，根据你使用的SMTP支持情况选择一种
    # 普通方式，通信过程不加密
    # smtp = smtplib.SMTP(smtpHost, smtpPort)
    # smtp.ehlo()
    # smtp.login(username, password)

    # tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
    # smtp = smtplib.SMTP(smtpHost,smtpPort)
    # smtp.set_debuglevel(True)
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    # smtp.login(username,password)

    # 纯粹的ssl加密方式，通信过程加密，邮件数据安全
    smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
    smtp.ehlo()
    tsmtp.login(username,password)

    # 发送邮件
    w = smtp.sendmail(fromMail, toMail, mail.as_string())
    print('ok')
    smtp.close()

except Exception as e:
    print(e)