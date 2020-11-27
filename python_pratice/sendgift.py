"""
发礼物的例子：
1.拥有一个礼物的标识
2.定义一个发礼物的方法
3.定义一个展示礼物的方法
4.启动方法
"""
##拥有礼物的方法
have_gift = False


##发礼物的方法
def send():
    print("发礼物啦")
    global have_gift
    have_gift = True


##展示礼物的方法
def show():
    if have_gift == True:
        print("收到礼物啦,么么哒")
    else:
        print("没有收到礼物")


if __name__ == '__main__':
    send()
    show()
