#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://cloud.tencent.com/developer/article/2149231',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Arcgis REST 服务目录浏览',

      'level'     :   'medium',

      'FOFA'      :   'title="ArcGIS"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/2',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/arcgis/rest/services'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200  and 'ArcGIS REST Services Directory' in res.text and re.search(r'Folder: /',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret