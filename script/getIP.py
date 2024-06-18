#coding:utf-8
#author:胖胖小飞侠
import socket
from urllib.parse import urlparse
def main(url):
	try:
		parsed_result = urlparse(url)
		domain = parsed_result.hostname
		ip = socket.gethostbyname(domain)
		return ip
	except:
		pass
	return None
