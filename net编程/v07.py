import smtplib
from email.mime.text import MIMEText

'''
MIMEText:
    1. 邮件内容
    2. MIME子类型，plain表示text类型
    3. 邮件编码格式
'''
msg = MIMEText('python 邮件','plain','utf-8')

from_addr = '497124007@qq.com'
from_pwd = 'anyhwjvigfnpbice'

to_addr = '497124007@qq.com'

# 腾讯邮箱的smtp地址
smtp_srv = 'smtp.qq.com'

try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)

    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print('异常:',e)

