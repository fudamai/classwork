#! python
# -*- coding:utf-8 -*-
# Author:fudamai
# email.py


"email学习"

import smtplib
from smtplib import SMTP_SSL  # 安全加密
from email.header import Header  # 邮件标题
from email.mime.text import MIMEText  # 正文
from email.mime.multipart import MIMEMultipart  # 多部分时的基础类
from email.mime.base import MIMEBase  # 
from email import encoders  # 编码


class MailMaster:
    """邮箱大师"""
    def __init__(self, smtp_server='smtp.qq.com', email_addr='furight@foxmail.com', password=None):
        self.smtp = SMTP_SSL(smtp_server)
        # smtp.set_debuglevel(1)
        self.smtp.ehlo(smtp_server)
        self.smtp.login(email_addr, password)
        self.email_from = email_addr
        self.email_to = []

    def add_email_to_list(self, addr):
        """添加收件人"""
        self.email_to.append(addr)

    def notice(self, username, text, subject="通知信息"):
        """这是一个注册提醒，根据用户名更改正文的内容
        """
        self.send_email_all(subject, f'{username}\n' + text)
        pass

    def send_email_all(self, subject, body, mailtype='plain', attachment=None):
        """
        构造一个可以发HTML文本的函数
        subject: 标题
        body: 邮件内容
        mailtype： 邮件类型。默认是文本，发HTML时指定为HTML
        attachment: 附件
        """
        # 构造一个MIMEMultipart对象代表邮件本身
        msg = MIMEMultipart()

        msg["Subject"] = Header(subject, "utf-8")
        msg["from"] = self.email_from
        try:
            if len(self.email_to) > 0:
                to_mail = self.email_to
                msg['To'] = ','.join(to_mail)
            else:
                print('未添加收件邮箱')


            # mailtype代表邮件类型，纯文本或HTML等
            # 可更改
            msg.attach(MIMEText(body, mailtype, 'utf-8'))

            #有附加内容，才添加到邮件
            if attachment:
                with open(attachment, 'rb') as f:  # 二进制模式打开文件
                    # MIMEBase表示附件的对象
                    mime = MIMEBase('text', 'txt', filename=attachment)
                    # filename是显示附件名字
                    mime.add_header('Content-Disposition', 'attachment', filename=attachment)
                    # 获取附件内容
                    mime.set_payload(f.read())
                    encoders.encode_base64(mime)  # 编码
                    # 作为附件添加到邮件
                    msg.attach(mime)
            
            self.smtp.sendmail(self.email_from, self.email_to, msg.as_string())
            self.smtp.quit()
        except smtplib.SMTPException as e:
            print(e)



# class NoMailListError(Exception):
#     """
#     没有添加邮件列表返回的报错值
#     自定义报错类型
#     """
    # return break

def get_password():
    "返回授权码"
    return ''

def main():
    mail = MailMaster(password=get_password())
    # mail.add_email_to_list('2544272158@qq.com')  # 添加收信人
    # mail.add_email_to_list('mengcheng5@live.com')  # 添加收信人
    # mail.notice('王菲', '你的账号在内蒙古登录了')
    mail.send_email_all('通知','赶紧睡觉哦')

if __name__ == "__main__":
    main()