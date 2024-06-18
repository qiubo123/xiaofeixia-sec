#coding:utf-8
#根据url和poc生成全部需要执行的命令
import os
import json
import script.initPy as initPy
def main():
	all_poc = []
	file_path = os.getcwd() + os.sep + 'poc' +os.sep#poc的位置
	for root,dirs,files in os.walk(file_path):
		if '__pycache__' not in root:

			initPy.main(root)

		for file in files:
			if '.py' in file:
				if '__init__' not in file and '.pyc' not in file and '模板' not in file and 'randomcase' not in file and 'getIP.py' != file:
					poc = {}
					path = os.path.join(root,file)
					_poc_path_cmd = root.split('\\poc\\')[-1]
					if _poc_path_cmd == '':
						_poc_path_cmd = 'poc'
					else:
						_poc_path_cmd = 'poc.' + _poc_path_cmd
					_poc_file_cmd = '.' + file.split('.')[0]
					_poc_cmd = _poc_path_cmd + _poc_file_cmd
					poc['cmd'] = _poc_cmd
					poc['scrip_name'] = file
					poc['path'] = path

					all_poc.append(poc)
	_all_poc = []#存储全部信息
	for p in all_poc:
		import poc
		_poc = p['cmd']
		cmd = _poc+'.msg()'
		res = eval(cmd)
		p['method'] = res['method']
		p['level'] = res['level']
		p['bug_name'] = res['bugname']
		_all_poc.append(p)

	folders = ['config']
	for f in folders:
		if not os.path.exists(f):
			os.makedirs(f)
	with open('./config/poc.json','w',encoding='utf-8') as f:
		json.dump(_all_poc,f)
	
	return all_poc	