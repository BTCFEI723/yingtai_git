# 📊 你的当前提交树

"""""

bd22f43 (HEAD -> main) 版本1.4：新增jupyter，完善Git操作笔记
0208e87 版本1.3：更新Python笔记并备份旧版网页
5fc7f3f 完善Git操作命令注释
0a11e6e 版本1.2：标题字体3.8rem，补充Git diff/commit示例
b41c3ee 版本1.1：主题色改为粉色，添加站长姓名'樱泰'
c47c473 添加Python练习文件
d0211c8 添加 .gitignore 文件，忽略 PyCharm 配置
9bf13a5 初始提交：创建3D空间站

"""""

"""
🔄 回滚的三种类型与操作)

类型一：撤销工作区的修改（最轻量）
场景：你修改了文件但还没 git add，想放弃这些修改。

# 撤销指定文件的修改（恢复到最后一次提交或add的状态）
git restore 3d-space-station.html

# 撤销所有未暂存的修改
git restore .
"""

"""
场景2：从暂存区撤回文件（当你看到文件在"要提交的变更"列表中）

bash
# 假设 git status 显示：
#   新文件：   3d-space-station.html
# 那么运行：
git restore --staged 3d-space-station.html  # 从暂存区撤回，但保留工作区文件
"""

"""
类型三：撤销已提交的版本（核心回滚）

这是你最可能想了解的部分，有两种主要方法：

🎯 方法A：git revert - 安全回滚（推荐）

创建新的提交来撤销某次旧提交的更改，不会删除历史。

操作示例：
# 1. 回滚最近一次提交（撤销版本1.4）
git revert HEAD

# 2. 回滚特定提交（比如撤销版本1.1）
git revert b41c3ee

# 3. 回滚一个区间的提交（撤销多个）
git revert 0a11e6e..bd22f43  # 左开右闭，撤销从版本1.2到1.4的更改

执行 git revert HEAD 会发生什么：

Git会分析 bd22f43 这次提交改了哪些内容
创建一个新的提交，内容正好与 bd22f43 相反
你的提交历史会变成：

text
[新提交] Revert "版本1.4：新增jupyter，完善Git操作笔记"
bd22f43 版本1.4：新增jupyter，完善Git操作笔记
0208e87 版本1.3：...
...（之前的历史都在）

"""

"""
🎯 方法B：git reset - 重置历史（谨慎使用）

直接移动分支指针到某个旧提交，删除之后的提交历史。

三种模式：

bash
# 1. --soft 软重置：只移动指针，工作区和暂存区保持不变
git reset --soft 0a11e6e  # 回退到版本1.2，但保留所有修改在暂存区

# 2. --mixed 混合重置（默认）：移动指针，重置暂存区，保留工作区修改
git reset --mixed 0a11e6e  # 回退到版本1.2，修改留在工作区

# 3. --hard 硬重置（危险！）：彻底回到指定版本，丢弃所有修改
git reset --hard 0a11e6e  # ⚠️ 完全回到版本1.2的状态，版本1.3和1.4的修改会丢失！

"""


