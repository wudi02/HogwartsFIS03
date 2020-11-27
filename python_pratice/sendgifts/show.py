from gift import have_gift


##展示礼物的方法 进行条件判断
def show():
    if have_gift == True:
        print("收到礼物啦,么么哒")
    else:
        print("没有收到礼物")
