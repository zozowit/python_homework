# coding=utf-8

import os
import os.path

def key_print(file, key, dict_index):
    if len(dict_index) == 0:
        return
    print('在文件【%s】中找到关键字【%s】'%(file, key))
    for each in dict_index:
        print('关键字出现在第%d行， 第%s个位置'%(each, str(dict_index[each])))
    print('============================================')

def key_save(file, key, line_list):
    if len(line_list) == 0:
        return
    file_name = file + '.' + key + '.txt'
    print('save to %s'%(file_name))

    f = open(file_name, 'w', encoding='gb18030', errors='ignore')
    f.writelines(line_list)
    f.close()

def key_search(file, key, need_print, need_save):
    line_num = 0
    count = 0
    start = 0
    last_index = 0
    
    line_list = []


    key_len = len(key)

    (name, ext) = os.path.splitext(file)

    if ext == '.py':
        return
#    f = open('C:\\Python36\\test\\record.txt')
    f = open(file, encoding='gb18030', errors='ignore')

    for each_line in f:
        index = each_line.find(key, start)

        if index != -1:
            line_list.append(each_line+'\n')

    f.close()

    key_save(file, key, line_list)

def search_file(key, need_print, need_save):
    file_list = []
    
    for root, dirs, files in os.walk(os.curdir):
        for each in files:
            print(each)
            
            temp_str = os.path.join(root, each)
            print(temp_str)
            key_search(temp_str, key, need_print, need_save)

def main():

    b_need_save = True
    key = input('请将改脚本放于带查找的文件夹内，请输入关键字：')

    search_file(key, False, True)
main()
