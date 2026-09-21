import json

# # 成绩表数据
# json 文件没有元组类型，写入 json 的时候，元组会自动变成列表[]。
# 读取回来json.load()拿到的永远是列表，不再是元组。
# score_list = [
#     {"学号": "S001", "姓名": "王林", "语文": 85, "数学": 92, "英语": 78},
#     {"学号": "S002", "姓名": "李慕婉", "语文": 92, "数学": 88, "英语": 95},
#     {"学号": "S003", "姓名": "十三", "语文": 78, "数学": 85, "英语": 82},
#     {"学号": "S004", "姓名": "曾牛", "语文": 88, "数学": 79, "英语": 91},
#     {"学号": "S005", "姓名": "周轶", "语文": 95, "数学": 96, "英语": 89},
#     {"学号": "S006", "姓名": "王卓", "语文": 76, "数学": 82, "英语": 77},
#     {"学号": "S007", "姓名": "红蝶", "语文": 89, "数学": 91, "英语": 94},
#     {"学号": "S008", "姓名": "徐立国", "语文": 75, "数学": 69, "英语": 82},
#     {"学号": "S009", "姓名": "许木", "语文": 86, "数学": 89, "英语": 98},
#     {"学号": "S010", "姓名": "通天", "语文": 66, "数学": 59, "英语": 72}
# ]

# # 生成json文件
# with open(r"../resources/score.json", "w", encoding="utf‑8") as file:
#     json.dump(score_list, file, indent=4, ensure_ascii=False)
#
# print("✅ score.json 文件生成成功！")

# 案例



# 读取json文件的成绩表来解决以下问题

with open(r"../resources/score.json", "r", encoding="utf‑8") as f:
    student_data = json.load(f)
# 1．计算每个学生的总分、各科平均分，然后一并输出出来。
print("\n=====1.每个学生总分、平均分=====")
for student in student_data:
    # 计算总分
    total_score = student["语文"] + student["数学"] + student["英语"]
    # 计算平均分
    average_score = total_score / 3
    # 输出结果
    print(f"{student['姓名']}的总分为{total_score},平均分为{average_score}")
# 2．统计各科成绩的最低分、最高分、平均分，并输出。
print("\n=====2.各科成绩的最低分、最高分、平均分=====")
print("\n=====2.各科最低、最高、平均分=====")
chinese = [i["语文"] for i in student_data]
math = [i["数学"] for i in student_data]
english = [i["英语"] for i in student_data]
print(f"语文：最低{min(chinese)}，最高{max(chinese)}，平均{sum(chinese)/len(chinese):.2f}")
print(f"数学：最低{min(math)}，最高{max(math)}，平均{sum(math)/len(math):.2f}")
print(f"英语：最低{min(english)}，最高{max(english)}，平均{sum(english)/len(english):.2f}")
# 3．查找成绩优秀（平均分大于 90）的学生，并输出。
print("\n=====3.优秀学生（平均分>90）=====")
for s in student_data:
    avg_score = (s["语文"] + s["数学"] + s["英语"]) / 3
    if avg_score > 90:
        print(f"{s['学号']} {s['姓名']} 平均分{avg_score:.2f}")