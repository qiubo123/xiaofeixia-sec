#coding:utf-8
#自动生成__init__.py文件
import os
def main(path):#自动生成__init__.py文件
	imps = []
	init_py = os.path.join(path,'__init__.py')
	_im = path.strip('\\').split('\\')[-1]
	for f in os.listdir(path):
		_path = os.path.join(path,f)
		if '__init__.py' not in _path:
			if '__pycache__' not in _path:
				if '.txt' not in _path and '_poc_模板' not in _path and ' 'not in _path and '.war' not in _path and '原神启动' not in _path:
				#如果有文件不想被import，从这里添加排除
					if os.path.isfile(_path):
						imp = 'from . ' + 'import ' + f.replace('.py','')
					if os.path.isdir(_path):
						imp = 'import ' + _im + '.' + f
					if imp not in imps:
						imps.append(imp)

	with open(init_py,'w',encoding='utf-8') as f:
		for i in imps:
			f.write(i)
			f.write('\n')