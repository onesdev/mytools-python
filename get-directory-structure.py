"""
根据当前目录下的目录结构，自动生成markdown格式的文件索引
这里我们使用Path类取代os中的路径和文件函数，好处是在输入输出路径时不需要考虑windows或posix格式了
"""


from pathlib import Path

class Folder:
    def __init__(self, path, level, blackfolders=set(), blackfiles=set()):
        self.path = path  # 当前目录的绝对路径
        self.level = level  # 目录深度，0表示根目录，1表示1级子目录，2表示2级子目录。。。
        self.blackfolders = blackfolders
        self.blackfiles = blackfiles
        self.child_folders = []  # 当前目录下的子目录列表（Folder对象）
        self.child_files = []  # 当前目录下的子文件列表（文件的Path对象）
        self.get_childs()

    # 获取当前目录下的所有子节点（目录和文件）
    def get_childs(self):
        self.child_folders = []
        self.child_files = []
        for child in self.path.iterdir():
            if child.is_dir():
                self.child_folders.append(Folder(child, self.level+1, self.blackfolders))
            elif child.is_file():
                self.child_files.append(child)

    def write_index_md(self, outputfile):
        for file in self.child_files:
            if str(file.name) not in self.blackfiles:
                outputfile.write(f"[{file.name}]({str(file)})\r\n\r\n")

        header = '#' * (self.level+1)
        for folder in self.child_folders:
            if folder.path.name not in self.blackfolders:
                outputfile.write(f"{header} {folder.path.name}\r\n\r\n")
                folder.write_index_md(outputfile)

# 读取当前目录的目录结构，输出到index.md
blackfolders = {'assets'}  # 不打印到index.md的目录集合
blackfiles = {'.DS_Store', 'get_directory_structure.py', 'index.md'}  # 不打印到index.md的文件集合
f = Folder(Path("."), 0, blackfolders, blackfiles)
with open("index.md", mode='w') as outputfile:
    f.write_index_md(outputfile)
