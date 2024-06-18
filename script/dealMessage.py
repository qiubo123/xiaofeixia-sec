#coding:utf-8
#处理脚本执行后的返回值
import datetime
import script.recordlog as recordlog
# import script.sendmail as sendmail
from colorama import init,Fore
init(autoreset=True)
def main(res):
	# print(res)
	bugif = res['ifbug']
	if bugif == False:
		return False
	if bugif == True:
		_bug_url = res['url']
		_bug_name = res['bugname']
		_bug_level = res['level']
		_bug_links = res['links']
		_bug_method = res['method']
		_bug_huixian = res['huixian']
		today = datetime.date.today()
		_found_time = datetime.datetime.now().strftime('%H:%M:%S')
		found_time = Fore.BLUE+ str(today) + ' ' + str(_found_time) + Fore.RESET
		bug_method = Fore.MAGENTA + _bug_method + Fore.RESET
		bug_level = Fore.RED + _bug_level + Fore.RESET
		bug_url = Fore.YELLOW + _bug_url + Fore.RESET
		bug_name = Fore.GREEN + _bug_name + Fore.RESET
		bug_msg = f'[{found_time}] [{bug_method}] [{bug_level}] {bug_name} {bug_url}'
		log_msg = f'[{_found_time}] [{_bug_name}] {_bug_url} '
		recordlog.log(log_msg)

		content = """
###############皮皮虾-sec发现漏洞###############

漏洞名称：{bugname}

漏洞地址：{url}

漏洞级别：{level}

发现时间：{found_time}

回显：{huixian}

参考链接：{links}

请及时查看和处理!
################################################
""".format(url=bug_url,bugname=bug_name,level=bug_level,links=_bug_links,found_time=found_time,huixian=_bug_huixian)
		return content
		subject = '小飞侠-发现漏洞信息！请注意！'
		result = sendmail.sendMsg(subject,content)
		if result == True:
			msg = bug_msg + "\t邮件发送成功！"
		else:
			msg =  bug_msg + "\t未发送邮件"
		return msg

