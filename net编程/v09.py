import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase, MIMEMultipart

mail_mul = MIMEMultipart()

mail_text = MIMEText('邮件正文', 'plain', 'utf-8')

mail_mul.attach(mail_text)

with open('02.html','rb') as f:
    s = f.read()
    m = MIMEText(s, 'base64', 'utf-8')
    m['Content-Type'] = 'application/object-stream'
    m['Content-Disposition'] = "attachment; filename='02.html'"

    mail_mul.attach(m)

from_addr = '497124007@qq.com'
from_pwd = 'anyhwjvigfnpbice'

to_addr = '497124007@qq.com'

smtp_srv = 'smtp.qq.com'

try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)

    srv.sendmail(from_addr,[to_addr],mail_mul.as_string())
    srv.quit()
except Exception as e:
    print('异常:',e)