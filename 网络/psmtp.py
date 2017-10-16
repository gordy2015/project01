#! /usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import sys

mail_host = 'smtp.ruaaji.cn'
mail_user = 'abc@ruaaji.cn'
mail_pass = '888888
mail_postfix = 'ruaaji.cn'
ssl_port = 465

def send_mail(to_list,subject,content):
    me = mail_user+"<"+mail_user+"@"+mail_postfix+">"
    print(me)
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list

    try:
        # s = smtplib.SMTP()
        # s.connect(mail_host)
        # s.login(mail_user,mail_pass)

        s = smtplib.SMTP_SSL(mail_host, ssl_port)
        s.ehlo()
        s.login(mail_user, mail_pass)

        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False

if __name__ == "__main__":
    t = input('To:')
    s = input('subject:')
    c = input('content:')
    send_mail(t,s,c)
    # send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
