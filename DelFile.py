import os
import shutil


# 判断该目录下是否有文件，有则删除，目的保留最新生成的文件
def delete_file():
    # deList = []
    # 需要清理的文件目录
    delDir = "path"
    deList = os.listdir(delDir)
    for f in deList:
        fileDir = os.path.join(delDir, f)
        if os.path.isfile(fileDir):
            os.remove(fileDir)
            print(fileDir + " was removed!")
        elif os.path.isdir(fileDir):
            shutil.rmtree(fileDir, True)
            print("Directory: " + fileDir +" was removed!")
