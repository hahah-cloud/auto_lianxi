import requests
from zuoye26.case.mokuai1.demo import KeCheng
import pytest
s = requests.session()

@pytest.fixture(scope="session")
def login_fix():
    k=KeCheng(s)
    k.login(s)
    return k

@pytest.fixture(scope="function")
def unlogin_fix():
    s.headers.update({'Authorization': 'Token 05cfe82b0c63688effcbbbe74135350ae1'})
    return s

