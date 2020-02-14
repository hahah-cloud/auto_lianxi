import requests


s = requests.session()
class KeCheng(object):
    def __init__(self,s,host="http://49.235.92.12:9000"):
        self.host=host
        self.s=s

    def login(self,s):
        url = self.host+"/api/v1/login"
        body = {
            "username": "test",
            "password": "123456"
        }
        r = self.s.post(url, json=body)
        print(r.json())
        token = r.json()["token"]
        h = {
            "Authorization": "Token %s" % token
        }
        self.s.headers.update(h)

    def update_info_1(self,test_input,expect):
        '''修改本人信息'''
        #ogin(self.s)
        url=self.host+"/api/v1/userinfo"
        body={
            "name":"test",
            "sex":test_input,
            "age":20,
            "mail":"283340479@qq.com"
        }
        r=self.s.post(url,json=body)
        print(r.json())
        return r.json()
        # assert r.json()["message"]=="update some data!"
        # assert r.json()["code"]==0

    def update_info_2(self, name="testx"):
        '''修改不是本人的信息'''
        url = self.host+"/api/v1/userinfo"
        body = {
            "name": name,
            "sex": "M",
            "age": 20,
            "mail": "283340479@qq.com"
        }
        r = self.s.post(url, json=body)
        print(r.text)
        return r.json()

    def test_info_35(self):
        '''登录不成功'''
        url=self.host+"/api/v1/userinfo"
        r=self.s.get(url)
        print(r.text)
        return r.json()



    def register(self):
        url=self.host+"/api/v1/register"
        body={
            "username":"test112",
            "password":"123456",
            "mail":"1233@qq.com"
        }
        r=self.s.post(url,json=body)
        print(r.json())


if __name__ == '__main__':
    k=KeCheng(s)
    res=k.register()








