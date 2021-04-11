import yaml

import pytest
#获取yaml文件以字典或列表取出

def get_datas():
    with open("test.yaml") as  f:
        datas = yaml.safe_load(f)
    return datas


class TestCase:


    def setup(self):
        #实例化类级别
        self.case1 = Calculator()
        print("开始测试")

    @pytest.mark.parametrize("a,b,c",get_datas()["add"]["datas"],ids=get_datas()["add"]["ids"])
    def test_add(self, a, b, c):
        assert round(self.case1.add1(a, b),2)== c #相加结果截取后2位数字


    @pytest.mark.parametrize("a,b,c", get_datas()["sub"]["datas"])
    def test_sub(self, a, b, c):
        assert self.case1.subtraction(a, b) == c

    @pytest.mark.parametrize("a,b,c", get_datas()["mul"]["datas"] )
    def test_mul(self,a, b, c):
        assert self.case1.multiply(a, b) == c

    @pytest.mark.parametrize("a,b,c", get_datas()["div_errpr"]["datas"] )
    def test_div_errpr(self, a, b, c):
        with pytest.raises(ZeroDivisionError):#除数为0异常处理
            self.test_div(a, b,c)

    @pytest.mark.parametrize("a,b,c", get_datas()["div"]["datas"] )
    def test_div(self,a, b, c):
        assert self.case1.divide(a, b) == c



    def teardown(self):
        print("测试结束")
