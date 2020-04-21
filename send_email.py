import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from docxtpl import DocxTemplate
from random import randint
from time import strftime, localtime


class QQEmail:

    def __init__(self, user, pwd, to):

        self._user = user
        self._pwd = pwd
        self._to = to

    def send_email(self, files, subject="", text=""):
        # 如名字所示Multipart就是分多个部分
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = self._user
        msg["To"] = self._to
        # ---这是文字部分---
        part = MIMEText(text)
        msg.attach(part)
        # ---这是附件部分---
        for file in files:
            part = MIMEApplication(open(file, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=file)
            msg.attach(part)

        s = smtplib.SMTP("smtp.qq.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
        s.login(self._user, self._pwd)  # 登陆服务器
        s.sendmail(self._user, self._to, msg.as_string())  # 发送邮件
        s.close()

    def create_word(self, digit):

        if digit == 2:
            low = 10
            upper = 99
            han_digit = "两"
        else:
            low = 100
            upper = 999
            han_digit = "三"
        randomNumberGroup = []

        for i in range(19):
            a = randint(low, upper)
            b = randint(low, upper)
            while abs(a - b) < 10 ** (digit - 1):
                b = randint(low, upper)
            item = {'a': a,
                    'b': b,
                    'plus': a + b,
                    'subtract': a - b,
                    'divide': round(a / b, 3)}
            randomNumberGroup.append(item)
        tpl_result = DocxTemplate('template_result.docx')
        tpl = DocxTemplate('template.docx')
        date = strftime("%Y-%m-%d", localtime())
        context = {'digit': han_digit,
                   'randomNumberGroup': randomNumberGroup,
                   'date': date}

        tpl.render(context)
        tpl_result.render(context)
        word_name = f'速算技巧练习（{han_digit}位数）.docx'
        word_name_result = f'速算技巧练习（{han_digit}位数）答案.docx'
        tpl.save(word_name)
        tpl_result.save(word_name_result)

        return [word_name, word_name_result]




