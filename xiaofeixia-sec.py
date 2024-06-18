#coding:utf-8
'''

'''
import sys
import script.options as options
import script.choiceOption as choice
import script.execOnePoc as execOnePoc
import script.dealMessage as dealMsg
import script.banner as banner
from concurrent.futures import ThreadPoolExecutor
import time
import signal
def signal_handler(signal,frame):
	print('\nSignal Catched! You have just type Ctrl+C!')
	sys.exit(0)
def main():
	signal.signal(signal.SIGINT,signal_handler)
	banner
	args = options.main()#根据参数执行相应功能
	dkej = choice.main(args)
	num = len(dkej)
	print(f'执行总任务数量：{num}')
	result_list = []
	if dkej != []:
		pool = ThreadPoolExecutor(30)#创建线程资源池
		n = 0
		for i in dkej:
			# print(i)
			# pool.submit(execute_one_poc,i)
			n = n + 1
			future = pool.submit(execOnePoc.main,i)
			# future_list.append(future)
			# print(future.result())
			msg = dealMsg.main(future.result())
			if msg != False:
				print('                                                    ',end='\r')
				print(msg)
			print(f'已完成进度 [ {n} / {num} ]',end='\r')

		pool.shutdown(wait=True)#等待所有线程执行完毕
		# print()
		if num == n:
			print('\n执行完毕！')
if __name__ == '__main__':
	main()