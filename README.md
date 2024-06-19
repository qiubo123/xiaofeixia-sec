
```

##
请在存在授权且合法的情况下使用该脚本，仅限学习交流使用，作者不支持任何违法犯罪行为。

使用注意点：
1、只要不删除、增加、修改poc的文件名，都不需要“-up”。
2、增加、删除poc,或者修改poc的文件名，都需要执行“-up”
3、可以在poc目录下移动poc至你认为合适的目录下，只要在移动后执行“-up”即可
4、由于个人精力有限，现有poc未一一验证，存在误报或poc错误的情况；
##
##
安装python模块
pip inssstall -r requirements.txt
或者指定源安装
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
用法示例
1、对一个网站执行所有poc
python xiaofeixia-sec.py -u http://www.tesssst.com -a
2、匹配某些poc进行扫描
python xiaofeixia-sec.py -u http://www.tesssst.com -s 弱口令
3、批量poc扫描(不支持同时匹配,目前只能匹配一个关键字，如：-s tomcat nginx是不支持的)
python xiaofeixia-sec.py -f targets.txt -s tomcat
4、扫描到的漏洞会记录到log目录下的文件，按照日期命名;
5、“-pl”列出当前所有的poc信息;
6、“debug”只能输出部分语法错误，这部分以后改进;
7、第一次扫描前需要执行“-up”读取poc并生成配置文件，这点很重要。
8、需要配置邮箱和授权码，最好是qq邮箱，其他的没配置，发现漏洞后可以直接邮件通知，不需要一直盯着;
9、邮件发送过快可能会被qq限制，导致收不到邮件;
##
```


```
poc编写规范
一般在弱口令poc中要获取location,
if res.status_code == 302 and '/out/out.ViewFolder.php' in res.headers['location']
需要指定allow_redirects=False，如下
res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False,allow_redirects=False)

```
##
如果需要dnslog，脚本里需要引入
import script.DnsLog as dnslog
dnslog.get_domain()#返回domain和cookie

用法：domain,cookie = dnslog.get_domain()
dnslog.get_result(domain,cookie)#传入domain和cookie两个参数，参数从get_domain()获取。返回True或False,True表示检测到回显，False表示未检测到回显
用法：
if dnslog.get_result(domain,cookie) == True:
	print('存在漏洞')#具体用法根据poc进行修改
##

如果需要获取网站IP，可以在脚本内任意poc导入
import script.getIP as getIP
def run():
	ip = getIP.main(url)
	if ip == None:#如果返回None,则代表未获取到IP地址，可以直接返回ret信息了。
	    return ret
	#继续检测



poc分类优先级
##
除OA、CMS外，其它均按照现有类型分类

##用法##
如果poc的数量或名称有变动，需要先执行`-up`更新配置文件
如果执行无任何输出则可能语法有误，可尝试执行`-debug`来调试

有漏洞的返回值里必须有url,无漏洞的可以没有，即
ret['url'] = url1

如有问题请与小飞侠联系，支持请点个star
请联系：3484762639#qq.com（所有数字减1并将#替换为@）
```
