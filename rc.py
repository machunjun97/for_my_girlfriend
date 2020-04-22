from time import sleep
from send_email import QQEmail
from os import remove
import schedule


def job():
    user = ""
    password = ""
    to = ""

    subject = "速算练习"
    text = "祝宝贝天天开心！！！     from 爱你的宝贝"

    send_to_mxn = QQEmail(user=user, pwd=password, to=to)
    for digit in range(2, 4):
        files = send_to_mxn.create_word(digit)
        send_to_mxn.send_email(files=files, subject=subject, text=text)
        sleep(3)
        for file in files:
            remove(file)


if __name__ == '__main__':
    schedule.every().day.at("20:00").do(job)

    while True:
        schedule.run_pending()
        sleep(1)















