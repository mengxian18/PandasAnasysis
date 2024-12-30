import re

# 打开并读取提交信息文件
with open("commits.txt", "r", encoding="utf-8") as file:
    commits = file.readlines()

# 初始化统计变量
bug_commits = []
bug_count = 0

# 定义要统计的关键词
bug_keywords = ["Bug", "Fix", "Error", "Issue", "Problem"]

# 分析每条提交信息
for commit in commits:
    # 检查是否包含任何bug相关的关键词
    if any(re.search(rf"\b{keyword}\b", commit, re.IGNORECASE) for keyword in bug_keywords):
        bug_commits.append(commit.strip())
        bug_count += 1

# 打印分析结果
print(f"总Bug相关提交数: {bug_count}")
print("Bug相关提交示例:")
for bug_commit in bug_commits[:5]:  # 只打印前5个示例
    print(f"  - {bug_commit}")

# 打印更多分析结果
print("\n详细分析:")
for keyword in bug_keywords:
    keyword_count = sum(1 for commit in bug_commits if re.search(rf"\b{keyword}\b", commit, re.IGNORECASE))
    print(f"{keyword}: {keyword_count}")