from email.mime.text import MIMEText

main_content='''
    <!DOCTYPE html>
    <html lang = 'en'>
    <head>
        <meta charset='utf-8'>
        <title>Title</title>
    </head>
    
    <body>
    <h1>这是一封HTML格式的邮件</h1>
    </body>
    
    </html>
'''

msg = MIMEText(main_content,'html','utf-8')

from_addr = '497124007@qq.com'
from_pwd = 'anyhwjvigfnpbice'

to_addr = '497124007@qq.com'

smtp_srv = 'smtp.qq.com'

try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)

    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print('异常:',e)