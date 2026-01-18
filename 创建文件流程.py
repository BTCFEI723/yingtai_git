"""

# 创建名为 "my-first-project" 的文件夹
mkdir my-first-project

# 查看是否创建成功
ls

第3步：进入这个文件夹

bash
# 进入刚创建的文件夹
cd my-first-project

# 查看当前所在位置
pwd
# 输出类似：/Users/你的用户名/my-first-project

第4步：在文件夹内创建第一个文件

方法A：用 touch 创建空文件

bash
# 创建名为 hello.txt 的空文件
touch hello.txt

# 查看文件
ls
# 应该能看到 hello.txt
方法B：用 echo 创建有内容的文件

bash
# 创建有内容的文件
echo "Hello, World!" > hello.py

# 查看文件内容
cat hello.py
# 输出：Hello, World!
方法C：用 cat 创建多行文件

bash
# 创建多行内容的文件
cat > notes.txt << 'EOF'
这是我的第一个笔记文件
创建于：2025年1月
内容：学习终端命令
EOF

# 查看
cat notes.txt

第5步：创建更多文件和文件夹

bash
# 1. 创建子文件夹
mkdir docs
mkdir images
mkdir src

# 2. 在各个文件夹中创建文件
echo "# 文档" > docs/README.md
touch images/photo1.png
echo "print('Hello')" > src/main.py

# 3. 查看整个项目结构
ls -R  # 递归查看所有文件和文件夹

完整流程示例

bash
# 从头到尾的完整示例
cd ~  # 回到用户主目录
mkdir my-project  # 创建项目文件夹
cd my-project  # 进入项目
touch README.md  # 创建说明文件
echo "# My Project" > README.md  # 添加内容
mkdir src  # 创建源代码目录
echo "print('Hello')" > src/app.py  # 创建Python文件
mkdir data  # 创建数据目录
ls -la  # 查看所有文件和文件夹

命令	       作用	           示例
pwd	       查看当前目录	   pwd
ls	       列出文件	       ls -la
mkdir	   创建文件夹	       mkdir 文件夹名
cd	       切换目录	       cd 文件夹名
touch	   创建空文件	       touch 文件名
echo	   创建有内容的文件   echo "内容" > 文件名
cat	       查看/创建文件	   cat 文件名
rm	       删除文件	       rm 文件名
rmdir	   删除空文件夹	   rmdir 文件夹名
rm -rf	   强制删除	       rm -rf 文件夹名
cp	       复制文件	       cp 源文件 目标文件
mv	       移动/重命名文件   mv 旧名 新名

"""""

