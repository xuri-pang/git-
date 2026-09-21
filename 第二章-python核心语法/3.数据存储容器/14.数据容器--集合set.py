# 为什么要用集合?集合有什么特点?
# 场景:在业务中,需要定义一个变量,来批量储存用户手机号(唯一的)
    # 列表list,元组tuple都不可以,因为这两个类型是可以储存重复元素的,但是手机号是唯一的,
    # 所以要用到集合set,set会自动去重,储存不重复的元素
# 一.介绍
# 1.集合set是一个无序的,不重复,可修改的数据容器

# 代码演示:
# s1 = {"c","d","e","f","e"}
# print(s1)  #输出集合s1,自动去重操作
# 空集合
# s2 = set()   #空集合的定义不能用{},因为{}是字典的定义方式,集合需要用()

# 二.集合(set)-常见方法
# 1.添加元素: add()-------------------------------s1.add('t')
# 2.移除集合中的指定元素: remove()-------------------s1.remove('t')
# 3.随机删除集合中的元素并返回: pop()------------------s1.pop()
# 4.清空集合中的所有元素: clear()----------------------s1.clear()
# 5.求取两个集合的差集: difference()--------------------s1.difference(s2)
# 6.求取两个集合的交集: intersection()-------------------s1.intersection(s2)
# 7.求取两个集合的并集: union()---------------------------s1.union(s2)

# 代码演示:
s1 = {100,200,300,400,500,600,700,800,900}
# a = s1.add(1000)      # 原地改自己 → 返回 None，不要用变量接收
s1.add(1000)
print(s1)               #{800, 900, 100, 200, 1000, 300, 400, 500, 600, 700}输出是无序的
s1.remove(100)
print(s1)   #{800, 900, 200, 1000, 300, 400, 500, 600, 700}
c = s1.pop()             #随机删除集合中的元素并返回,可以用变量接收
print(c)   #随机少一个数
s1.clear()
print(s1)   #空集合
s1 = {100,200,300,400,500,600}
s2 = {500,600,700,800,900}
print(s1.difference(s2))  #去除s1中的s2有的元素         这些求取
print(s1.intersection(s2))  #求取s1和s2的交集
print(s1.union(s2))  #求取s1和s2的并集

# ------------------------------------------三.案例------------------------------------
# 根据提供的班级选课情况,完成以下需求
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1.找出同时选修了法语和艺术的学生（交集）
# 方式一:
fa_set = french_set.intersection(art_set)
print("1.1 同时选法语和艺术的学生：", fa_set)

# 方式二:
fa_set2 = french_set & art_set
print("1.2 同时选法语和艺术的学生：", fa_set2)

# 2.找出同时选修了所有四门课程的学生（四门集合连续求交集）
# 方式一:
all_set = french_set.intersection(art_set).intersection(football_set).intersection(basketball_set)
print("2.1 同时选四门课程的学生：", all_set)
# 方式二:
all_set2 = french_set & art_set & football_set & basketball_set
print("2.2 同时选四门课程的学生：", all_set2)

# 3.找出选修了足球，但是没有选修篮球的学生（差集）
# 方式一:
fb_set = football_set.difference(basketball_set)
print("3.1 选足球不选篮球：", fb_set)
# 方式二: - 运算符可以来计算差集合
fb_set2 = football_set - basketball_set
print("3.2 选足球不选篮球：", fb_set2)
# 方式三:集合推导式------>快速构建集合,语法:{要往集合中添加的数据 for s in set1 if 条件}
fb_set3 = { s for s in football_set if s not in basketball_set}
print(f"3.3 选足球不选篮球： {fb_set3}")
# 4.统计每一个学生选修的课程数量
# 4.1 获取学生名单 -- 并集
# all_set = french_set.intersection(art_set).intersection(football_set).intersection(basketball_set  #方法一
# all_set = french_set & art_set & football_set & basketball_set   #方法二
all_set = french_set | art_set | football_set | basketball_set

# 4.2 获取每一个学生选修的课程数据
all_list = [*french_set, *art_set, *football_set, *basketball_set]   #解包

for s in all_set:
    print(f"4.1 {s} 选修的课程：", all_list.count(s))  #count统计出现了多少次
