﻿# SMTP를 통해 메일 전송을 해보자
# pip install smtplib

from smtplib import SMTP
from email.mime.text import MIMEText

src_email = 'city7312@naver.com'
dst_email = 'city7310@naver.com'

smtp = SMTP('smtp.naver.com', 587)
# SMTP 클래스의 인스턴스

smtp.starttls()
# tls가 필요한 경우

smtp.login('city7312', 'password')
# 로그인

message = MIMEText('내용내용', _charset='utf-8')
message['subject'] = '제목'
message['from'] = src_email
message['to'] = dst_email
# MIMEText 클래스를 이용해 제목, 송신자, 수신자를 설정

smtp.sendmail(src_email, dst_email, message.as_string())
smtp.quit()
