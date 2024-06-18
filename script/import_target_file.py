#coding:utf-8
#导入目标地址文件
import os
import urllib.parse
from urllib.parse import urljoin
def main(f):
	urls = []
	if os.path.exists(f):
		if os.path.isfile(f):
			with open(f,'r',encoding='utf-8') as f:	
				for u in f:
					url = u.strip('\n')
					if 'http' not in url:
						url = f'http://{url}'
					_url = urllib.parse.urlparse(url)
					url = _url.scheme + '://' + _url.netloc
					if url not in urls:		
						urls.append(url)
			return urls
		else:
			print('{} is not filetype,please check it!'.format(f))
			exit()
	else:
		print('{} does not exitst,please check it!'.format(f))
		exit(0)