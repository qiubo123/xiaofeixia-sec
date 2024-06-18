#coding:utf-8
#根据日期，将漏洞记录到当天日期的日志中，记录漏洞地址和名称
def getfilename():#构造文件名,形如：20230823-log.txt
	import datetime
	import os
	if not os.path.exists('log'):
		os.makedirs(log)
	today = datetime.datetime.today().strftime("%Y%m%d")
	logfilename = today + '_log.txt'
	return 'log'+os.sep+logfilename
def log(msg):
	flog = getfilename()
	with open(flog,'a+',encoding='utf-8') as f:
		f.write(msg)
		f.write('\n')