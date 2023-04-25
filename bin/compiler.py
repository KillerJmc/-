import sys

# 关键字替换表
# 还有部分不支持：[assert, async, await, class, def, del, except, finally, from, global,
#               import, lambda, nonlocal, raise, try, with, yield]
keywords = {
    "真": "True",
    "假": "False",

    "且": "and",
    "或": "or",
    "是": "is",
    "不是": "not",
    "当作": "as",

    "如果": "if",
    "要不然": "elif",
    "否则": "else",

    "对于": "for",
    "在": "in",
    "当": "while",
    "跳入下次循环": "continue",
    "跳出循环": "break",

    "无操作": "pass",
    "返回": "return",
    "空": "None",

    "函数": "def"
}

# 符号替换表
symbols = {
    '（': '(',
    '）': ')',
    '，': ',',
    '：': ':',
    '“': '"',
    '”': '"'
}

# 内置函数替换表
builtin_functions = {
    "打印": "print",
    "区间": "range",
    "转字符串": "str",
    "转整数": "int",
    "转小数": "float"
}


# 读取文件所有行到列表
def read_lines(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


# 将多行字符串输出到文件
def out_lines(file_path: str, lines: list[str]):
    with open(file_path, "w", encoding="utf-8") as f:
        return f.writelines(lines)


# 替换关键字
def replace_keywords(dj_lines: list[str]):
    for i in range(len(dj_lines)):
        line = dj_lines[i].replace("\n", "")
        words = line.split()
        indent = len(line) - len(" ".join(words))
        for j in range(len(words)):
            word = words[j]
            if word in keywords:
                words[j] = keywords[word]
        dj_lines[i] = " " * indent + " ".join(words)


# 替换符号
def replace_symbols(dj_lines: list[str]):
    for i in range(len(dj_lines)):
        line = list(dj_lines[i])
        for j in range(len(line)):
            symbol = line[j]
            if symbol in symbols:
                line[j] = symbols[symbol]
        dj_lines[i] = "".join(line)


# 替换内置函数
def replace_builtin_functions(dj_lines: list[str]):
    for i in range(len(dj_lines)):
        for chinese_name, origin_name in builtin_functions.items():
            dj_lines[i] = dj_lines[i].replace(chinese_name, origin_name)


# 是否是调试模式
debug = False

# 命令行参数列表
args = sys.argv

# 第一个参数是dj脚本的路径
dj_path = args[1]

# 获取dj脚本的所有行
dj_lines = read_lines(dj_path)

# 具体转化流程
replace_keywords(dj_lines)
replace_symbols(dj_lines)
replace_builtin_functions(dj_lines)

# 获取转化后的python脚本
py_code = "\n".join(dj_lines)

# 如果调试模式就只打印转化后python脚本的结果，否则直接执行。
if debug:
    print(py_code)
else:
    exec(py_code)


