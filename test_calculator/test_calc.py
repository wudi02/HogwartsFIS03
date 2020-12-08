import allure
import pytest
import yaml

from calculator_code.calc import Calculator


class TestCalc:
    @pytest.mark.run(order=1)
    @allure.story("测试加法")
    @pytest.mark.add
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            with allure.step("计算两个数相加"):
                # 调用add方法
                result = get_calc.add(get_add_datas[0], get_add_datas[1])
            # 判断result是浮点数，则保留2位小数
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
            # 得到结果之后，要写断言
            assert result == get_add_datas[2]

    @pytest.mark.run(order=4)
    @allure.story("测试除法")
    @pytest.mark.div
    def test_div(self, get_calc, get_div_datas):
        result = None
        try:
            with allure.step("计算两个数相除"):
                result = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            assert result == get_div_datas[2]

    @pytest.mark.run(order=2)
    @allure.story("测试减法")
    @pytest.mark.sub
    def test_sub(self, get_calc, get_sub_datas):
        result = None
        try:
            with allure.step("计算两个数相减"):
                result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            assert result == get_sub_datas[2]

    @pytest.mark.run(order=3)
    @allure.story("测试乘法")
    @pytest.mark.mul
    def test_mul(self, get_calc, get_mul_datas):
        result = None
        try:
            with allure.step("两个数相乘"):
                result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            assert result == get_mul_datas[2]
