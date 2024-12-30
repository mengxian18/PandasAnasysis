import requests
import certifi
# 忽略证书验证，通过requests.get()方法获取数据
# 获取提交信息 
url = "https://api.github.com/repos/pandas-dev/pandas/commits"
headers = {
    "Authorization": "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",  # 替换为你的实际访问令牌
    "Accept": "application/vnd.github.v3+json"
}

commits = []
page = 1
per_page = 100

while len(commits) < 1000:
    response = requests.get(f"{url}?per_page={per_page}&page={page}", headers=headers, verify=False)
    if response.status_code == 200:
        page_commits = response.json()
        if not page_commits:
            break
        commits.extend(page_commits)
        page += 1
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        break

# 打开一个文件以写入提交信息
with open("commits.txt", "w", encoding="utf-8") as file:
    # 遍历所有提交信息
    for commit in commits[:1000]:
        # 获取提交信息的消息
        message = commit['commit']['message']
        # 将提交信息写入文件
        file.write(message + "\n")

print("提交信息已保存到 commits.txt 文件中。")