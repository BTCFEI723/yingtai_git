# git add git_tutorial.py
# git commit -m "添加结构化的Git教程脚本"
# cat > git_tutorial.py << 'EOF'
#!/usr/bin/env python3
"""
Git教程 - 结构化版本
用Python类组织学习内容
"""

class GitTutorial:
    """Git教程主类"""
    
    def __init__(self):
        self.sections = {
            "基础操作": self.basics,
            "分支管理": self.branching,
            "合并与冲突": self.merging,
            "高级技巧": self.advanced,
        }
    
    def basics(self):
        """基础操作"""
        return {
            "初始化": "git init",
            "配置用户": "git config --global user.name '你的名字'",
            "添加文件": "git add 文件名",
            "提交更改": "git commit -m '描述'",
            "查看状态": "git status",
            "查看历史": "git log --oneline",
        }
    
    def branching(self):
        """分支管理"""
        return {
            "查看分支": "git branch",
            "创建分支": "git branch 新分支",
            "切换分支": "git checkout 分支名",
            "创建并切换": "git checkout -b 新分支",
            "删除分支": "git branch -d 分支名",
        }
    
    def merging(self):
        """合并与冲突"""
        return {
            "合并分支": "git merge 分支名",
            "解决冲突步骤": [
                "1. 编辑冲突文件",
                "2. 删除冲突标记(<<<<<<<, =======, >>>>>>>)",
                "3. 保留想要的内容",
                "4. git add 文件名",
                "5. git commit",
            ],
            "放弃合并": "git merge --abort",
        }
    
    def advanced(self):
        """高级技巧"""
        return {
            "暂存更改": "git stash",
            "恢复暂存": "git stash pop",
            "查看差异": "git diff",
            "撤销修改": "git checkout -- 文件名",
            "重写历史": "git rebase -i HEAD~3",
        }
    
    def display(self):
        """显示所有内容"""
        for section_name, section_func in self.sections.items():
            print(f"\n=== {section_name} ===")
            content = section_func()
            
            if isinstance(content, dict):
                for key, value in content.items():
                    if isinstance(value, list):
                        print(f"\n{key}:")
                        for item in value:
                            print(f"  {item}")
                    else:
                        print(f"{key}: {value}")
            print()

# 使用教程
if __name__ == "__main__":
    tutorial = GitTutorial()
    tutorial.display()
