import money


def select():
    if money.saved_money == 1000:
        print(f"工资还没到账啊 要吃土土了,现在工资是{money.saved_money}")
    else:
        money.saved_money == 2000
        print(f"工资到账了,但是太少了,现在工资是:{money.saved_money}")
