import re
from collections import defaultdict

# 打开并读取提交信息文件
with open("commits.txt", "r", encoding="utf-8") as file:
    commits = file.readlines()

# 初始化统计变量
matthew_commits = []
matthew_keyword_count = defaultdict(int)

# 定义要统计的关键词及其含义
keywords = {
    "DOC": "文档相关的更改",
    "Fix": "修复问题或错误的提交",
    "TST": "测试相关的更改",
    "Add": "添加新功能或新代码的提交",
    "Update": "更新现有功能或代码的提交",
    "DEPR": "弃用某些功能或代码的提交",
    "CI": "持续集成相关的更改",
    "Refactor": "重构代码的提交",
    "Enhance": "增强或改进现有功能的提交",
    "Bug": "修复bug的提交",
    "Performance": "性能优化相关的提交",
    "Security": "安全相关的更改",
    "Revert": "回滚之前的提交"
}

# 分析每条提交信息
for i in range(len(commits)):
    commit = commits[i]
    # 检查是否由Matthew Roeschke参与
    if "Matthew Roeschke" in commit:
        # 提取包含上下文的提交信息
        context = "\n".join(commits[i-2:i+3]).strip()
        matthew_commits.append(context)
        
        # 统计关键词出现次数
        for keyword in keywords:
            if re.search(rf"\b{keyword}\b", commit, re.IGNORECASE):
                matthew_keyword_count[keyword] += 1

# 打印Matthew Roeschke的贡献总结
print(f"Matthew Roeschke的总提交数: {len(matthew_commits)}")
for keyword, count in matthew_keyword_count.items():
    print(f"{keyword} ({keywords[keyword]}): {count}")

print("\nMatthew Roeschke的贡献示例:")
for commit in matthew_commits[:170]:  # 打印示例
    print(f"  - {commit}\n")
# 将打印的这些贡献示例保存到一个文本文件中，以便后续使用。
# 打开一个文件以写入贡献示例
with open("MatthewRoeschke_contributions.txt", "w", encoding="utf-8") as file:
        file.write("Matthew Roeschke的贡献示例:\n")
        for commit in matthew_commits:
            file.write(f"{commit}\n\n")