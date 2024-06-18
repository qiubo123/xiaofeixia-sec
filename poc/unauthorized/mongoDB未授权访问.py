#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
import script.getIP as getIP
import pymongo
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'MongoDB未授权访问',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/25',
  }
  return ret
def run(url,ua):
  ret = msg()
  ip = getIP.main(url)
  if ip == None:
    return ret
  url1 = f'mongodb://{ip}:27017/'
  ret['url'] = url1
  try:
    client = pymongo.MongoClient(url1,serverSelectionTimeoutMS=5000)
    dbs = client.list_database_names()
    if len(dbs) > 0:
      ret['huixian'] = url
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret