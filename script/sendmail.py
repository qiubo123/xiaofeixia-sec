#coding:utf-8
def sendMsg(z,m):#传入主题和正文内容
	import os
	now_path = os.path.dirname(os.path.abspath(__file__))
	real_path = os.path.realpath(now_path)#当前路径的绝对路径
	conf = real_path + os.sep + 'setting.conf'
	import smtplib
	from email.mime.text import MIMEText
	import configparser
	config = configparser.ConfigParser()
	config.read(conf,encoding='utf-8')
	msg_from = config.get('mail','mail_from')
	passwd = config.get('mail','password')
	msg_to = config.get('mail','mail_to')
	content = m#正文内容
	msg = MIMEText(content)
	msg['Subject'] = z#主题
	msg['From'] = msg_from
	msg['To'] = msg_to
	try:
		s = smtplib.SMTP_SSL("smtp.qq.com",465)
		s.login(msg_from, passwd)
		# s.ehlo()
		s.sendmail(msg_from,msg_to,msg.as_string())
		s.quit()
		# print("邮件发送成功，请查收！")
		return True
	# except:	
	# 	print('发送失败')
	except s.SMTPException as e:
		print('发送失败',e)
		# pass
	# finally:
		# s.quit()  
	
# sendMsg('a','b')