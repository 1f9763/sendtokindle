#coding=utf-8
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import Encoders

if len(sys.argv)!=2:
    sys.exit('argv error')
else:
    try:
        EMAIL_FROM='nexus10@163.com'
        EMAIL_TO='nexus10@163.com'
        EMAIL_SERVER='smtp.163.com'

        msg = MIMEMultipart()
        msg['Subject'] = 'test'
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO

        filename=sys.argv[1].split('\\')[-1]
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(unicode(sys.argv[1],'utf-8'), "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition','attachment',filename=filename)

        msg.attach(part)

        server = smtplib.SMTP(EMAIL_SERVER)
        server.login('nexus10@163.com','buxuewushu163')
        server.sendmail(EMAIL_FROM,EMAIL_TO, msg.as_string())
    except Exception,e:
        print str(e)