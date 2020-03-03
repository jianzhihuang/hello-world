#!/usr/bin/env python3
# coding=utf-8
import os
path=input('請輸入文件路徑：')+"//"
#獲取該目錄下所有文件，存入列表中 
f = os.listdir(path)
n = 0 
for i in f: 
 #設置舊文件名（就是路徑+文件名） 
 oldname=path+f[n] #設置新文件名
 newname=path+'a'+str(n+1)+'.log' 
 #用os模塊中的rename方法對文件改名 
 os.rename(oldname,newname) 
 print(oldname,'已經改名為：',newname) 
 n+=1
