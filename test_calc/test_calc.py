import pytest
import yaml

from calculator_code.calc import Calculator

with open("./datas/calc.yml") as f:
    # add_datas = yaml.safe_load(f)['add']
    data = yaml.safe_load(f)
    add_datas = data['add']['datas']
    add_myid = data['add']['add_myid']
    div_datas = data['div']['datas']
    div_myid = data['div']['div_myid']


def test_a():
    print("这是测试用例--加法除法")


class TestCalc:

    def setup_class(self):
        print("开始计算")
        # 实例化计算器的类
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a,b,expect", add_datas, ids=add_myid
    )
    def test_add(self, a, b, expect):
        # 实例化计算器的类
        # calc = Calculator()
        # 调用add方法
        result = self.calc.add(a, b)
        # 判断result是浮点数，则保留2位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，要写断言
        assert result == expect

    @pytest.mark.parametrize(
        "c,d,expect", div_datas, ids=div_myid
    )
    def test_div(self, c, d, expect):
        result = self.calc.div(c, d)
        if isinstance(result, float):
            result = round(result, 2)
            assert result == expect

    # def test_add1(self):
    #     # 实例化计算器的类
    #     # calc = Calculator()
    #     # 调用add方法
    #     result = self.calc.add(0.1, 0.1)
    #     # 得到结果之后，要写断言
    #     assert result == 0.2
    #
    # def test_add2(self):
    #     # 实例化计算器的类
    #     # calc = Calculator()
    #     # 调用add方法
    #     result = self.calc.add(-1, -1)
    #     # 得到结果之后，要写断言
    #     assert result == -2
