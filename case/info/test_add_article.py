import allure

@allure.feature("测试添加文章接口")
class TestAdd():

    @allure.story("验证是否添加且显示正确")
    @allure.issue("http://49.235.92.12:8080/zentao/bug-browse-2.html")
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-374-1.html")
    def test_add_article(self,login_fix):
        '''用例描述'''
        k=login_fix
        result=k.add_article(title="test文章7")
        actul=k.get_add_article(result)
        assert actul=="test文章7"



