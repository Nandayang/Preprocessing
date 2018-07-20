# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:29:43 2018

@author: yang
"""

import os;
import pypinyin
from pypinyin import pinyin

 
def main(path):     
    filelist=os.listdir(path)
    for files in filelist:
        Olddir=os.path.join(path,files);
        if os.path.isdir(Olddir):
     
            continue;
        filename=os.path.splitext(files)[0]; 
        filename1 = pinyin(filename, style=pypinyin.FIRST_LETTER) 
        filename2 = []
        for i in filename1:
            lenth = 0
            for j in i[0] :
                lenth += 1
            if lenth>1:
                filename2.extend(i)
        filenameToStr = ''.join(filename2) 
        filetype=os.path.splitext(files)[1];   
        Newdir=os.path.join(path,filenameToStr + filetype);
        os.rename(Olddir,Newdir);
print("--enter the file_path--")
i = input()
main(i)
print("Processing completed")
os.system("pause")