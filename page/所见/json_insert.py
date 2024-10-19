import json
from os.path import exists
from datetime import datetime

# 新条目
new_entry = {
    "NAME": "Looking For Cats In a Badly Drawn City",
    "RATE": "3.5",
    "TIME": "2024.10.19-21:32",
    "TYPE": "Game",
}

# 文件路径
file_path = "所见.json"


def insert_entry(file_path, new_entry):
    time_format = "%Y.%m.%d-%H:%M"

    # 尝试解析新条目的时间，如果失败则抛出异常
    try:
        new_time = datetime.strptime(new_entry["TIME"], time_format)
    except ValueError:
        raise ValueError(f"时间格式错误: {new_entry['TIME']}")

    # 如果文件存在，加载数据；否则初始化为空字典
    if exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = {}

    # 如果新条目的类型不存在于数据中，则添加该类型
    data.setdefault(new_entry["TYPE"], [])

    # 获取当前类型的条目列表
    entries = data[new_entry["TYPE"]]

    # 查找新条目应该插入的位置
    for i, entry in enumerate(entries):
        existing_time = datetime.strptime(entry["TIME"], time_format)
        if new_time > existing_time:
            entries.insert(i, new_entry)
            break
    else:  # 如果没有找到合适的位置，则添加到列表末尾
        entries.append(new_entry)

    # 将更新后的数据写回文件
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"已将新条目 {new_entry} 插入到 {file_path}")


# 调用函数插入新条目
insert_entry(file_path, new_entry)
