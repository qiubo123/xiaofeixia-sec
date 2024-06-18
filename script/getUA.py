#coding:utf-8
#生成随机USER agent
def get_ua():
  import random
  first_num = random.randint(55, 62)
  third_num = random.randint(0, 3200)
  fourth_num = random.randint(0, 140)
  os_type = [
    '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)',
    '(Macintosh; Intel Mac OS X 10_12_6)','(Windows NT 10.0; Win64; x64)'
  ]
  chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

  ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
           '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
          )
  return ua