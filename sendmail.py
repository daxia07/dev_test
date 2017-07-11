#!/usr/bin/env python
# encoding: utf-8
# copyright reserved by futu5.com

"""
@version: 2.0
@author: alienz
@license: Apache Licence 
@contact: limingxia07@gmail.com
@site: http://www.futu5.com
@software: PyCharm
@file: sendmail.py
@time: 2017/7/7 18:15
"""

from datetime import datetime
import smtplib
import time

__author__ = "alienz"

def notifymail(receiver,subject,msg,sender='13087920164@163.com',sender_pwd="fttest177"):
    """
    This function send notify mail from sender to receiver for given subject and msg
    :param sender: sender mail, default was set as 163 mailbox
    :param receiver: mail address to receive the mail 
    :param subject: mail subject
    :param msg: mail message
    :param sender_pwd: password to login
    """
    host = "smtp.163.com"
    port = "25"
    mail_subject = subject
    mail_txt = "App daily_task @" + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mail_body = "\r\n".join((
            "From: %s" % sender,
            "To: %s" % receiver,
            "Subject: %s" % mail_subject,
            "",
            mail_txt, msg
    ))
    server = smtplib.SMTP()
    server.connect(host,port)
    server.login(sender,sender_pwd)
    server.sendmail(sender,receiver,mail_body)
    server.quit()

if __name__ == '__main__':
    while True:
        dt = list(time.localtime())
        cur_hour = dt[3]
        cur_minute = dt[4]
        if cur_minute == 0:
            notifymail("tshlmx@qq.com","NEW TEST","Time to have a rest!")
            time.sleep(60)
