import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText('Hello world', 'plain', 'utf-8')

header_from = Header('测试邮件<497124007@qq.com>', 'utf-8')
msg['From'] = header_from

header_to =Header('发送到自己的qq邮箱','utf-8')
msg['To'] = header_to

header_subject = Header('这是摘要','utf-8')
msg['Subject'] =header_subject

from_addr = '497124007@qq.com'
from_pwd = 'anyhwjvigfnpbice'

to_addr = '497124007@qq.com'

smtp_srv = 'smtp.qq.com'

try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)

    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print('异常:',e)
