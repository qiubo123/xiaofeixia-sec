#coding:utf-8
def randomLowercase(n):#返回特定长度的随机小写字母
	import random
	import string
	lst = []
	for j in range(n):
		lst.append(random.choice(string.ascii_lowercase))
	lowercase = ''.join(lst)
	return lowercase
def randomInt(n,m):#返回某个范围中的int
	import random
	return random.randint(n,m)
def hashmd5(s):
	import hashlib
	md5 = hashlib.md5()
	md5.update(str(s).encode('utf-8'))
	str_md5 = md5.hexdigest()
	return str_md5[0:15]
hashmd5(123456)
def substr(s,n,m):#返回字符串s的切片截取
	return s[n:m]

def base64Str(n):
	import base64
	base64str = str(base64.b64encode(n.encode('utf-8'))).lstrip("b'").rstrip("'")
	return base64str
base64Str('admin')
#常用正则
#root:.*?:[0-9]*:[0-9]*:
#re.search(r'uid.*?gid.*?groups.*?',res.text,re.S)

# 'for 16-bit app support'
# #取数据
# result = re.search(r'<div class="line2">(?P<md5_str>.*?)</div>',res.text,re.S)
# print(result.group('md5_str'))


# import re
# text = '''
# "code":1,
# "data":ico_afaefoijoaeif.jsp
# '''
# res = re.search(r'code.*?data.*?:(?P<filename>.*?).jsp',text,re.S)
# print(res.group('filename'))