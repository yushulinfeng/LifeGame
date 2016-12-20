#!/usr/bin/python
# -*- coding: utf-8 -*-

import zipfile   
import os.path   

#解决办法：file()改为open()

'''文件解压工具类'''
'''python的注释写在代码后面'''

class UnzipFile(object):
    '''文件解压工具类'''
    def __init__(self, filename, mode='r', basedir=''):   
        self.filename = filename   
        self.mode = mode   
        if self.mode in ('w', 'a'):   
            self.zfile = zipfile.ZipFile(filename, self.mode, compression=zipfile.ZIP_DEFLATED)   
        else:   
            self.zfile = zipfile.ZipFile(filename, self.mode)   
        self.basedir = basedir   
        if not self.basedir:   
            self.basedir = os.path.dirname(filename)   
          
    def close(self):   
        self.zfile.close()   
          
    def extract_to(self, path):   
        for p in self.zfile.namelist():   
            self.extract(p, path)   
              
    def extract(self, filename, path):
        if not filename.endswith('/'):
            f = os.path.join(path, filename)
            d = os.path.dirname(f)
            if not os.path.exists(d):
                os.makedirs(d)
            open(f, 'wb').write(self.zfile.read(filename))


def unzip(zfile, path):
    # 将指定zip压缩文件解压到指定目录，目录不存在将会被创建
    # 要解压的文件不存在，或者解压失败，将返回false
    if not os.path.exists(zfile):
        return False
    try:
        z = UnzipFile(zfile)
        z.extract_to(path)
        z.close()
    except:
        return False
    return True


if __name__ == "__main__":
    # TEST
    print (unzip("d:\\123.zip", "d:\\123456798"))



    
