#coding:utf-8
#获取dnslog,如果有自建的dnslog服务器，可以改为自己的
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
import os
import time
import script.getUA as ua
def get_domain():
	headers = {
		'User-Agent': ua.get_ua(),
		'Referer':'http://dnslog.cn/'
	}
	url = 'http://dnslog.cn/getdomain.php?t=0.09594455458721185'
	try:
		res=requests.get(url=url,headers=headers,timeout=10,verify=False)
		domain = res.text.strip()
		cookie = res.headers['Set-Cookie'].split(';')[0].strip()
		result = (domain,cookie)
		return result
	except:
		pass
# dnslog()
def get_result(domain,cookie):
	headers = {
		'User-Agent': ua.get_ua(),
		'Cookie':cookie,
		'Accept': '*/*',
		'Referer':'http://dnslog.cn/',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9',
	}
	url = f'http://dnslog.cn/getrecords.php?t=0.9043777403415532'
	# print(domain)
	try:
		r=requests.get(url=url,headers=headers,timeout=20,verify=False)
		# print(r.text)
		if '[]' != r.text and domain in r.text:
	 		 return True
		else:
			return False
	except:
		# print("[!!!]  dnslog.cn刷新dnslog失败")
		pass
	return False
def resp(domain):
	domain = f'http://{domain}'
	headers = {'User-Agent': ua.get_ua(),}
	try:
		res=requests.get(url=domain,headers=headers,timeout=10,verify=False)
		print(res.status_code)
		print(res.text)
	except:
		pass
# domain,cookie = get_domain()
# print(domain)
# print(cookie)
# time.sleep(10)
# resp(domain)#模拟请求
# # os.system(f'curl -I http://{domain}')
# time.sleep(5)
# if get_result(domain,cookie):
# 	print('[+]打dnslog成功')
# else:
# 	print('[-]打dnslog失败')
# # get_result(1,2)



