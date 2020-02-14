from zuoye26.case.mokuai1.demo import KeCheng
from zuoye26.common.read_ya import readyml
import pytest
import requests
s=requests.session()

#@pytest.mark.parametrize("test_input,expect",
  #                       [("M",{'message': 'update some data!', 'code': 0}),
   #                      ("F",{'message': 'update some data!', 'code': 0}),
    #                      ("x",{'message': '参数类型错误', 'code': 3333})])

test_data=readyml("test_da.yml")["update_info"]
@pytest.mark.parametrize("test_input,expect",test_data)
def test_update_info(login_fix,test_input,expect):
    res=login_fix.update_info_1(test_input,expect)
    assert res["message"] == expect["message"]
    assert res["code"]==expect["code"]

def test_update_info_2(login_fix):
    res=login_fix.update_info_2()
    assert res["message"] == "无权限操作"


def test_unlogin(unlogin_fix):
    s=unlogin_fix
    k=KeCheng(s)
    rs=k.test_info_35()
    assert rs["detail"]=="Invalid token."


''' 1、import数据库py文件 
    2、写数据库语句 ，作为前置函数
    3、test开头的用例里，传入前置函数为参数
    同一账号不能重复注册，要删除'''
def  test_register():
    pass
