"""""
一、 基础终端命令（先熟悉环境）

在操作 Git 前，先了解几个最基本的终端命令，它们能帮你“找到和看清”文件。

命令	            全称/解释	                示例	     作用
pwd	            Print Working Directory	    pwd	     查看当前所在目录的绝对路径。
ls	            List	                    ls	     列出当前目录下的文件和文件夹（不包括隐藏文件）。
ls -a	        List All	                ls -a	 列出所有内容，包括以 . 开头的隐藏文件（如 .git）。
cd <路径>	    Change Directory	        cd Documents	切换目录到指定路径。cd .. 返回上一级。
mkdir <名称>	    Make Directory	            mkdir my_project 创建新文件夹。
touch <文件名>	-	                        touch readme.md	 创建新文件。
cat <文件名>	    Concatenate	                cat readme.md	 查看文件内容。
clear 或 Cmd+K	-	                        clear	       清空当前终端屏幕（内容还在，只是往上滚了）。

"""""

"""
二、 Git 核心工作流命令（日常使用频率最高）

这是最核心的部分，对应 Git 的本地工作流程。

阶段	          命令	               示例	                  作用与说明
初始化	      git init	           git init	              在当前目录创建全新的 Git 仓库。
克隆	          git clone <仓库地址>  git clone https://...  下载一个已有的远程仓库到本地。
检查状态	      git status	       git status	          查看当前仓库的状态（哪些文件被修改、已暂存等）。最常用，有疑问就先执行它。
添加到暂存区	  git add <文件>	       git add .	          将文件的改动添加到暂存区。git add . 添加所有改动。
提交到仓库	  git commit -m “描述”  git commit -m “修复登录bug”	将暂存区的改动正式提交到本地仓库，并附上说明。
查看历史	      git log	            git log --oneline	   查看提交历史记录。--oneline 参数可以让输出更简洁。


"""

"""
三、 Git 分支与远程操作命令

当你需要并行开发或团队协作时，这些命令至关重要。

类别	          命令	                      示例	                 作用与说明
分支管理	      git branch	              git branch	         列出所有本地分支，当前分支前有 * 号。
              git branch <分支名>	      git branch feature-1	 创建新分支。
              git checkout <分支名>	      git checkout main	     切换到指定分支。
              git checkout -b <分支名>	  git checkout -b hotfix	创建并立即切换到新分支（常用组合）。
              git merge <分支名>	          git merge feature-1	 将指定分支合并到当前分支。
远程操作	      git remote -v	              git remote -v	         查看已关联的远程仓库地址（通常叫 origin）。
              git push origin <分支>   	  git push origin main	 将本地提交推送到远程仓库。
              git pull origin <分支>	      git pull origin main	 从远程仓库拉取最新更新到本地并合并。
撤销与对比	  git diff	                  git diff	             查看工作区与暂存区文件的差异（具体改了哪些代码）。
              git restore <文件>	          git restore readme.md	 丢弃工作区的改动（让文件回到最后一次 add 或 commit 的状态）。
              
              
                练习3：交互式查看历史

                bash
                # 图形化查看历史
                git log --oneline --graph --all
                
                # 查看文件变化历史
                git log --oneline -- 3d-space-station.html
                练习4：清理测试文件
                
                bash
                # 如果之前创建了test.txt等测试文件
                git status
                # 删除不需要的文件
                rm -f test.txt *.tmp
                git status

                📝 实用命令备忘单
                
                场景	命令
                安全撤销提交	git revert <commit>
                查看简洁历史	git log --oneline -10
                查看图形历史	git log --oneline --graph --all
                比较两个版本	git diff <commit1> <commit2>
                创建新分支	git checkout -b <分支名>
                切换分支	git checkout <分支名>
                当前状态	git status
                
                🕰️ 1. git log - 提交历史时间轴

                    这是最常用的时间线查看方式，记录所有正式的提交。
                    
                    基础时间线查看：
                    
                    bash
                    # 按时间倒序列出提交（最新在最上面）
                    git log
                    
                    # 简洁模式（更适合快速浏览）
                    git log --oneline
                    
                    # 带分支图的完整时间线
                    git log --oneline --graph --all
                    
                    按时间范围筛选：
                    
                    bash
                    # 查看最近3次提交
                    git log -3
                    git log --oneline -5
                    
                    # 查看某个时间之后的提交
                    git log --since="2026-01-10"
                    
                    # 查看某个时间段的提交
                    git log --since="2026-01-10" --until="2026-01-15"
                    
                    # 查看昨天到今天的提交
                    git log --since="yesterday"
                    git log --since="1 week ago"
                    
                    按作者/内容筛选：
                    
                    bash
                    # 查看特定作者的提交
                    git log --author="樱泰"
                    
                    # 搜索提交信息中包含关键词的
                    git log --grep="revert"
                    
                    # 查看涉及某个文件的提交历史
                    git log -- 3d-space-station.html
                    
                    # 查看文件的内容变化时间线
                    git log -p -- 3d-space-station.html
                    
                    2. git reflog - 操作记录时间轴
                    
                    这是Git的“黑匣子”或“时间机器”，记录你执行的所有Git操作。
                    
                    查看完整操作历史：
                    
                    bash
                    # 查看所有操作记录（按执行时间倒序）
                    git reflog
                    
                    # 查看main分支的操作记录
                    git reflog show main
                    
                    # 查看HEAD的操作记录
                    git reflog show HEAD


"""

# .gitignore：这是要创建的文件名。以点开头在Unix系统中是隐藏文件。


"""# 1. 进入你的练习文件夹
cd ~/Desktop/git-practice

# 2. 初始化Git仓库（如果还没做）
git init

# 3. 添加3D网页文件
git add 3d-space-station.html

# 4. 第一次提交
git commit -m "初始版本：创建带3D效果的太空主题网页"

# 5. 修改文件后查看变化
git status
git diff

# 6. 提交修改
git add 3d-space-station.html
git commit -m "设计更新：优化卡片阴影和动画效果"

# 查看当前分支（现在应该显示 main）
git branch

# 查看详细的提交历史
git log --oneline

# 查看仓库状态
git status
"""

"""
推荐操作步骤

第1步：创建 .gitignore 文件（最重要）

这个文件告诉Git哪些文件/文件夹不应该跟踪。用以下命令创建：

bash
# 创建 .gitignore 文件
echo ".idea/" > .gitignore

# 查看文件内容确认
cat .gitignore
这会在你的文件夹里创建一个 .gitignore 文件，里面只有一行 .idea/，表示忽略整个 .idea 文件夹

"""

"""

第2步：添加 .gitignore 文件到Git

bash
git add .gitignore
git commit -m "添加 .gitignore 文件，忽略 PyCharm 配置"
"""

"""

第3步：处理Python文件（二选一）

选项A：如果想管理Python文件（推荐，可以练习更多）

bash
# 添加所有Python文件（不包括.idea/）
git add *.py

# 提交
git commit -m "添加Python练习文件"


git add *.py
*.py：这是一个通配符。

* 表示“任意字符”或“任意数量的字符”。
.py 表示“以 .py 结尾”。
所以 *.py 组合起来的意思是：“所有以 .py 结尾的文件”。

"""

# echo "*.py" >> .gitignore
# >>：这也是一个重定向操作符，但和 > 有区别。
#
# >：覆盖文件（清空原内容，写入新内容）。
# >>：追加到文件末尾（保留原内容，在最后添加新行）。
# "*.py"：要追加的内容，表示“忽略所有 .py 文件”。
# 执行后：用 cat .gitignore 查看，文件现在应该有两行：
#
# text
# .idea/
# *.py

# # 查看哪些文件被修改了
# git status
#
# # 查看具体改了哪些代码（高亮显示）
# git diff
#
# # 添加修改
# git add 3d-space-station.html
#
# # 提交新版本
# git commit -m "版本1.1：优化UI颜色与文案"

# 最简单的方法：一次性提交所有修改
#
# bash
# # 1. 添加当前目录下所有已修改的文件到暂存区
# git add .
#
# # 2. 提交这些修改
# git commit -m "版本1.2：增大标题字体，完善Git操作笔记"

# 第三步：验证提交
#
# bash
# # 查看提交历史
# git log --oneline
#
# # 或查看最近一次提交的详情
# git show HEAD


"""方法	命令	效果	风险	推荐度
git log --oneline 先确认版本
只查看	git show 9bf13a5:3d-space-station.html	终端显示内容	无风险	⭐⭐⭐⭐
创建副本	git show 9bf13a5:3d-space-station.html > 旧版.html	生成新文件	无风险	⭐⭐⭐⭐⭐
"""

"""
# 撤销Python文件的修改（回到上次提交的状态）
git restore "示例1-1 git操作命令清单.py"

# 删除新增的HTML文件（如果不需要）
rm "旧版.html"
"""