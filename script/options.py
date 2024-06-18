#coding:utf-8
#指定脚本参数信息
import argparse
def main():
	parser = argparse.ArgumentParser(description='帮助信息！如有问题可联系胖胖小飞侠解决')
	parser.add_argument('-u','--url',type=str,required=False,help='目标地址')
	parser.add_argument('-s','--search',type=str,required=False,help='搜索poc的关键字')
	parser.add_argument('-p','--poc',type=str,required=False,help='指定poc')
	parser.add_argument('-a','--all-poc',action='store_true',default=False,help='执行全部poc')
	parser.add_argument('-f','--file',type=str,help='指定存在目标url的txt文件')
	parser.add_argument('-up','--updata-poc',action='store_true',default=False,help='更新poc配置，新增、减少poc或者更改poc的名字都需要手动执行此参数，更改poc内容不需要！')
	parser.add_argument('-pl','--poc-list',action='store_true',default=False,help='列出所有poc信息')
	parser.add_argument('-debug',action='store_true',default=False,help='如果脚本没有任何输出，一般为脚本出现语法错误，请直接使用此参数！')
	args = parser.parse_args()
	return args