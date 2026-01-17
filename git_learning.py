# 创建git_learning.py文件

# !/usr/bin/env python3
"""
Git学习笔记 - Python版本
避免Jupyter笔记本的合并冲突问题
"""


# 第一部分：基础命令
def git_basics():
    """Git基础命令"""
    commands = {
        "初始化仓库": "git init",
        "查看状态": "git status",
        "添加文件": "git add <文件名>",
        "提交更改": "git commit -m '提交信息'",
        "查看历史": "git log --oneline",
        "查看所有分支": "git branch",
        "创建分支": "git branch <分支名>",
        "切换分支": "git checkout <分支名>",
        "创建并切换": "git checkout -b <新分支名>",
        "合并分支": "git merge <分支名>",
        "删除分支": "git branch -d <分支名>",
    }

    print("=== Git基础命令 ===")
    for desc, cmd in commands.items():
        print(f"{desc}: {cmd}")
    print()


# 第二部分：分支操作流程示例
def branch_workflow():
    """分支工作流程示例"""
    print("=== 分支工作流程 ===")

    workflow = [
        ("1. 在主分支工作", "git checkout main"),
        ("2. 创建新分支", "git checkout -b 新功能"),
        ("3. 在新分支开发", "# 修改文件，添加功能"),
        ("4. 提交更改", "git add . && git commit -m '添加新功能'"),
        ("5. 切换回主分支", "git checkout main"),
        ("6. 合并新功能", "git merge 新功能"),
        ("7. 删除临时分支", "git branch -d 新功能"),
    ]

    for step, action in workflow:
        print(f"{step}: {action}")
    print()


# 第三部分：合并冲突解决
def merge_conflict_resolution():
    """合并冲突解决方法"""
    print("=== 合并冲突解决 ===")

    steps = [
        "1. 合并时出现冲突: git merge 其他分支",
        "2. 查看冲突文件: git status",
        "3. 打开冲突文件，找到冲突标记:",
        "   <<<<<<< HEAD",
        "   当前分支的内容",
        "   =======",
        "   被合并分支的内容",
        "   >>>>>>> 其他分支",
        "4. 手动编辑文件，决定保留哪个版本",
        "5. 删除冲突标记，只保留想要的内容",
        "6. 标记冲突已解决: git add 文件名",
        "7. 完成合并: git commit",
    ]

    for step in steps:
        print(step)
    print()


# 第四部分：实用技巧
def git_tips():
    """Git实用技巧"""
    print("=== Git实用技巧 ===")

    tips = [
        "1. 查看简洁日志: git log --oneline --graph",
        "2. 撤销工作区修改: git checkout -- 文件名",
        "3. 撤销暂存区文件: git reset HEAD 文件名",
        "4. 查看文件差异: git diff",
        "5. 查看两个分支差异: git diff 分支1..分支2",
        "6. 查看操作记录: git reflog",
        "7. 恢复误删分支: git checkout -b 分支名 提交哈希",
        "8. 暂存当前工作: git stash",
        "9. 恢复暂存工作: git stash pop",
        "10. 重命名分支: git branch -m 旧分支名 新分支名",
    ]

    for tip in tips:
        print(tip)
    print()


# 第五部分：实际练习函数
def practice_exercise():
    """实际练习：模拟分支操作"""
    print("=== 实际练习：分支与合并 ===")

    # 模拟文件内容
    file_content = {
        "main": ["print('主分支的代码')", "# 这里是主分支"],
        "feature": ["print('功能分支的代码')", "# 这里是功能分支"],
    }

    print("初始状态：")
    print("main分支文件内容:")
    for line in file_content["main"]:
        print(f"  {line}")

    print("\nfeature分支文件内容:")
    for line in file_content["feature"]:
        print(f"  {line}")

    print("\n模拟合并（保留两者）:")
    merged = file_content["main"] + ["", "# 合并后的内容"] + file_content["feature"]
    for line in merged:
        print(f"  {line}")


# 运行所有示例
if __name__ == "__main__":
    git_basics()
    branch_workflow()
    merge_conflict_resolution()
    git_tips()
    practice_exercise()

    print("=== 学习完成！ ===")
    print("现在你可以用这个.py文件来记录Git学习笔记了！")
    print("好处：")
    print("1. 纯文本，不会像Jupyter那样有格式问题")
    print("2. Git合并时不会出现JSON冲突")
    print("3. 可以用任何文本编辑器编辑")
    print("4. 可以用Python的注释功能做笔记")
EOF

# 给执行权限
chmod + x
git_learning.py

# 添加到Git跟踪
git
add
git_learning.py
git
commit - m
"创建Git学习Python脚本"