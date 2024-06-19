#coding:utf-8
#根据option执行响应功能,最后返回执行的命令
import script.initCmds as pocs
import script.import_target_file as impfile
import urllib.parse
import json
import os
import sys
from colorama import Fore
def get_poc_cmd():
	f = 'config'+os.sep+'poc.json'
	if not os.path.exists(f):
		print('未读取到poc配置文件，请先更新poc配置，执行： python xiaofeixia-sec.py --updata-poc')
		sys.exit()

	with open(f,'r',encoding='utf-8') as f:
		data = json.load(f)
	return data
def main(args):
	target_url = vars(args)['url']
	if target_url != None and 'http' not in target_url:
		target_url = 'http://' + target_url
	poc_search = vars(args)['search']
	one_poc = vars(args)['poc']
	target_file = vars(args)['file']
	whether_all_poc = vars(args)['all_poc']
	whether_updata_poc = vars(args)['updata_poc']
	# print(whether_updata_poc)
	# shell_cmd = vars(args)['cmd']
	whether_debug =vars(args)['debug']
	poc_list = vars(args)['poc_list']
	target_urls = []
	target_pocs = []
	target_pocs = []
	if whether_debug == True:
		import poc#检查脚本中是否存在语法错误		
	if whether_updata_poc == True:
		count = len(pocs.main())
		print('\n\n\t\t-----poc已更新！-----\n')
		print('\n\t\t当前poc脚本总数为{}个'.format(count))
		sys.exit()
	if poc_list == True:
		with open('./config/poc.json','r',encoding='utf-8') as f:
			data = json.load(f)
			# print(data)
		js = 1
		for i in data:
			# print(i)
			_poc_name = i['bug_name']
			_poc_name = Fore.BLUE + _poc_name +Fore.RESET+' '
			_poc_method = '['+Fore.RED+i['method']+Fore.RESET+']'
			_poc_level = '['+Fore.YELLOW+i['level']+Fore.RESET+']'
			_poc = Fore.CYAN+str(js)+Fore.RESET+' '+ _poc_level + _poc_method + _poc_name 
			js=js+1
			print(_poc)
		sys.exit()
	if poc_search == None and one_poc == None and whether_all_poc == False:
		print('--> \n\n-->\t\t{}\n-->\n'.format('请使用"-a"、"-p"或者"-s"参数指定目标POC！'))
		sys.exit()

	_tps = get_poc_cmd()#获取所有poc
	_target_pocs = []
	for _tp in _tps:
		_cmd = _tp['cmd']
		_target_pocs.append(_cmd)
	# print(_target_pocs)
	if poc_search != None:
		target_pocs = []
		for c in _target_pocs:
			if poc_search in c and c not in target_pocs:
				print('--> \n-->\t\t{}\n-->\n'.format(c))
				target_pocs.append(c)
		if one_poc == None and whether_all_poc == False and target_url == None and target_file == None:
			print('\n\n{}\n{}\n'.format('未指定目标URL,请使用"-p"选项指定特定poc,如:python anyi-sec.py -t[-f] url/文件 -p poc.unauthorized.宝塔phpmyadmin未授权访问，','或使用"-s"选项匹配某些POC,使用方法和"-p"相同'))
			sys.exit()
	if one_poc != None:
		for c in _target_pocs:
			if one_poc == c:
				target_pocs = []
				target_pocs.append(c)
				break
	if whether_all_poc == True:
		target_pocs = _target_pocs
		# print(target_pocs)

	if target_url == None and target_file == None:
		print('\n--> \n-->\t\t{}\n-->\n'.format('请使用"-u"或者"-f"参数指定目标URL或者存放目标URL的txt文件名！'))
		sys.exit()

	if target_url != None:
		target_urls.append(target_url)
	if target_file != None:
		target_urls = impfile.main(target_file)
	
	dkej = []#笛卡儿积
	if target_urls != [] and target_pocs != []:
		new_targets = []
		for t in target_urls:
			_t = urllib.parse.urlparse(t)
			_t = _t.scheme + '://' + _t.netloc#只保留协议和域名
			new_targets.append(_t)
		for p in target_pocs:
			for url in new_targets:
				up = []
				up.append(url)
				up.append(p)
				dkej.append(up)
	return dkej