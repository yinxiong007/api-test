import os

def get_Path():
    #path = os.path.split(os.path.realpath(__file__))[0]
    path = os.path.abspath(os.path.dirname(__file__))
    return path

if __name__ == '__main__':# 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())
