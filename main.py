##Author:lclty(github.com/lclty OR space.bilibili.com/599302713)

import random
a = random.randint(1,41)
b = random.randint(1,41)
#草 突然想起来while这东西 试试看
while a == b:
    b = random.randint(1,41)

    


c = random.randint(1,41)
d = random.randint(1,41)
e = random.randint(1,41)

while c == a:
    while c == b:
        c = random.randint(1,41)

while d == a:
    while d == b:
        while d == c:
            d = random.randint(1,41)

while e == a:
    while e == b:
        while e == c:
            while e == d:
                e = random.randint(1,41)

#逻辑应该没错吧，如果再出现重复的那就本次作废然后手动筛选重复的

print("一等奖列表：序号"+str(a)+" 序号："+str(b))
print("二等奖列表：序号"+str(c)+" 序号："+str(d)+" 序号："+str(e))

#乐 基本print字符串连续法则忘了