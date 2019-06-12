import requests
import os
import smtplib
from email.mime.text import MIMEText

r=requests.get(url='https://m.ssrgo.ml/free_ssr')


smtp_server='smtp.163.com'
port=0
sender='wistar@163.com'
password='xx325622'
receiver='wistar.ma@gmail.com'

subject='test'
body=r.text
msg=MIMEText(body,'plain','utf-8')
msg['From']=sender
msg['To']=receiver
msg['Subject']=subject

print(body)
with smtplib.SMTP() as smtp:
    smtp.connect(smtp_server)
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,msg.as_string())
