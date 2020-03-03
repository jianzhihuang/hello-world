#!/usr/bin/env python3
# coding=utf-8
import os
 
#搜索包含的關鍵字
keyword = ['Package','[com.google.android.GoogleCamera]']
 
#搜索不包含的關鍵字
exclude_word = ['dog']
 
#設定一組指定的文件名擴展，用list方便添加其他類型文件
file_name_list = ['.v','.txt','.log']
 
#設定一組不搜索的文件名
exclude_file_name_list = []
 
#定義search函數，便於遞歸從文件中搜索關鍵字
def search(search_path):
 #判斷文件路徑是否存在
	if os.path.exists(search_path):
	#獲取search_name目錄下的文件/文件夾名，並遍歷文件
		for file_name in os.listdir(search_path):
			full_path = os.path.join(search_path,file_name)
			#flag 文件名是否包含file_name_list，不包含exclude_file_name_list
			flag = False
			 #flag_path 第一次打印文件名
			flag_filepath = True
			i = 0
			 #判斷是否是文件
			 ################
			 ###	非常重要  ######
			 ########################
			 ####這裏一定要用full_path，而不是file_name,否則出錯
			if os.path.isfile(full_path):
			   #判斷文件名中是否包含指定文件名
				for extend in file_name_list:
					if extend in file_name:
						flag = True
						#判斷文件名中是否不包含exclude_file_name_list中的文件名
						for exclude in exclude_file_name_list:
							if exclude in file_name:
								flag = False
				#如果flag為真，逐行檢索文件中的內容
				if flag:
					flag = False
					ff = open(full_path,'r')
					#逐行讀取文件內容，防止碰到大的文件卡死
					for line in ff:
						i+=1
						#是否打印改行標志位FLAG
						FLAG = False
						if len(exclude_word)==0:
							for KEY in keyword:
								if KEY in line:
								#改行滿足要求，打印
									FLAG = True
									break
						else:
							for KEY in keyword:
								if KEY in line:
									FLAG = True
									break									
							for UKEY in exclude_word:
								if UKEY in line:
									FLAG = False
									break
						if FLAG:
							FLAG = False
							#文件路徑只輸出一次，
							if flag_filepath:
								print("file path: "+full_path)
								flag_filepath = False
							print("line %d" %i)
							print(line)
			#如果是文件夾,遞歸調用search函數
			################
			 ###	非常重要  ######
			 ########################
			 ####這裏一定要用full_path，而不是file_name,否則出錯
			if os.path.isdir(full_path):
				search(full_path)
	else:
		print(search_path," not path ")
 
search_path = os.getcwd()
print(search_path)
search(search_path)
