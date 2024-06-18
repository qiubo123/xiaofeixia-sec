#coding:utf-8
#传入url和待检测的poc,执行一个poc,返回结果
import script.getUA as UA
def main(up):
	url = up[0]
	_poc = up[1]
	# print(_poc)
	ua = UA.get_ua()
	cmd = _poc+'.run("'+url+'","'+ua+'")'	
	import poc
	res = eval(cmd)#exec没有返回值
	return res