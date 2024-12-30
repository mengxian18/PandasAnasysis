import re

# 打开并读取提交信息文件
with open("commits.txt", "r", encoding="utf-8") as file:
    commits = file.readlines()

# 初始化统计变量
total_commits = len(commits)
word_count = 0
keyword_count = {}

# 定义要统计的关键词及其含义
keywords = {
    "DOC": "文档相关的更改，例如更新文档、修复文档错误等。",
    "Fix": "修复问题或错误的提交。",
    "TST": "测试相关的更改，例如添加或修改测试用例。",
    "Add": "添加新功能或新代码的提交。",
    "Update": "更新现有功能或代码的提交。",
    "DEPR": "弃用某些功能或代码的提交。",
    "CI": "持续集成相关的更改，例如修改CI配置。",
    "Refactor": "重构代码的提交。",
    "Enhance": "增强或改进现有功能的提交。",
    "Bug": "修复bug的提交。",
    "Performance": "性能优化相关的提交。",
    "Security": "安全相关的更改。",
    "Revert": "回滚之前的提交。"
}

# 分析每条提交信息
for commit in commits:
    # 统计字数
    words = commit.split()
    word_count += len(words)
    
    # 统计关键词出现次数
    for keyword in keywords:
        if re.search(rf"\b{keyword}\b", commit, re.IGNORECASE):
            if keyword in keyword_count:
                keyword_count[keyword] += 1
            else:
                keyword_count[keyword] = 1

# 打印分析结果
print(f"总提交数: {total_commits}")
print(f"总字数: {word_count}")
print("关键词统计:")
for keyword, count in keyword_count.items():
    print(f"{keyword} ({keywords[keyword]}): {count}")
# 将这个程序输出结果保存到一个新的文本文件中，命名为 count.txt。
# 打开一个文件以写入统计结果
with open("count.txt", "w", encoding="utf-8") as file:
    # 写入总提交数
    file.write(f"总提交数: {total_commits}\n")
    # 写入总字数
    file.write(f"总字数: {word_count}\n")
    # 写入关键词统计
    file.write("关键词统计:\n")
    for keyword, count in keyword_count.items():
        file.write(f"{keyword} ({keywords[keyword]}): {count}\n")
print("统计结果已保存到 count.txt 文件中。")
