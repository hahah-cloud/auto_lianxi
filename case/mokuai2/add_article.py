'''先登录
http://49.235.92.12:8020/xadmin/
admin yoyo123456
文章分类页面
http://49.235.92.12:8020/xadmin/hello/articleclassify/
新增一篇文章'''
import requests
import re
from requests_toolbelt import MultipartEncoder
from lxml import etree
import os
import allure

s=requests.session()

class Add(object):
    def __init__(self,s):
        self.s=s

    def login(self):
        url=os.environ["host"]+"/xadmin/"
        r=self.s.get(url)
        #print(r.text)
        token=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r.text)
        print(token[0])
        body={
            "csrfmiddlewaretoken":token[0],
            "username":"admin",
            "password":"yoyo123456",
            "this_is_the_login_form":1,
            "next":"/xadmin/",
        }
        r1=self.s.post(url,data=body)
        #print(r1.text)
        if "主页面 | 后台页面" in r1.text:
            print("登录成功")
        else:
            print("登录失败")

    @allure.step("添加文章")
    def add_article(self,title):
        url2=os.environ["host"]+"/xadmin/hello/articledetail/add/"
        r2=self.s.get(url2)
        token1=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r2.text)
        print(token1[0])
        m=MultipartEncoder(
                    fields=[
                        ("csrfmiddlewaretoken",token1[0]),
                        ("csrfmiddlewaretoken",token1[0]),
                        ("title",title),
                        ("auth","admin"),
                        ("classify","2"),
                        ("body","testssss测试"),
                        ("detail","测试备注备注"),
                        ("_save",""),])
        r3=self.s.post(url2,data=m,headers={'Content-Type':m.content_type})
        return r3.text

    @allure.step("获取已添加的文章名称字段")
    def get_add_article(self,result):
        demo=etree.HTML(result)
        node=demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
        print(node[0].text)
        return node[0].text



if __name__ == '__main__':
    os.environ["host"]="http://49.235.92.12:8020"
    k=Add(s)
    k.login()