import json
from pathlib import Path

# 写入json数据文件
user = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "hobbies": ["篮球", "足球", "羽毛球"]
}
json_file = Path(__file__).parent.parent / "resources" / "JSON" / "user.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(user, f, ensure_ascii=False, indent=4)   #ensure_ascii=False表示不转码，indent=4表示缩进4个空格

# 读取json数据文件
with open(json_file, "r", encoding="utf-8") as f:
    user = json.load(f)   #load的作用是直接将文本加载出来转化为python的对象
    print(user)           #这个对象是字典类型

