from time import sleep
from send_email import QQEmail
from os import remove
import schedule


def job():
    user = ""  # 发件人
    password = ""  # 密码
    to = ""  # 收件人

    date = time.strftime("%Y-%m-%d", time.localtime())
    subject = f"{date} 速算练习"  # 邮件标题
    text = "祝马晓娜天天开心，考公上岸！！！     from 爱你的宝贝"  # 邮件内容

    send_to_mxn = QQEmail(user=user, pwd=password, to=to)
    for digit in range(2, 4):
        files = send_to_mxn.create_word(digit)  # 生成速算表
        send_to_mxn.send_email(files=files, subject=subject, text=text)  # 发送邮件
        for file in files:
            remove(file)  # 删除生成的word文件


if __name__ == '__main__':
    schedule.every().day.at("20:00").do(job)  # 设定为每天20:00定时发送

    while True:
        schedule.run_pending()
        sleep(1)















