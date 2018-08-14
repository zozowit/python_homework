# -*- coding: utf-8 -*-

import os
import os.path
import easygui as g
import gzip as z

all_irq_dict = {}

def get_dir():
    path = g.diropenbox(msg='请选择log所在文件夹：', title='浏览文件夹')
	
    print('get_dir', path)
    return path

def show_result():
    all_text = ''
    cur_text = ''
    cur_statistic= ''

    print(all_irq_dict)
    for key in all_irq_dict:
        cur_text = ''
        value = all_irq_dict[key]
        
        cur_text = '文件名：' + key +'\n'
        for each in value:
            cur_text += 'IRQ[%s][%s]: %d times\n'%(each, value[each][1], value[each][0])
            
        all_text += cur_text

    g.textbox(msg='中断统计结果', title='统计结果', text=all_text)    

def try_unzip(file)

def key_search(file):
    irq_dict = {}

    key_gic = 'gic_show_resume_irq'
    key_system = 'pm_system_irq_wakeup'
    irq_num = ''
    irq_name = ''
    
    (name, ext) = os.path.splitext(file)

    if ext == '.txt':
        f = open(file, encoding='gb18030', errors='ignore')
    elif ext == '.gz':
        f = gzip.open(file, 'rb')
    else:
        return

    for each_line in f:
        index = each_line.find(key_gic)

        if index != -1:
            (a, irq_num, c, irq_name) = each_line[index:].split(' ', 3)
            print(irq_num, irq_name)

            if irq_num in irq_dict:
                irq_dict[irq_num][0] += 1
            else:
                irq_dict[irq_num] = [1, irq_name[: -1]]

            continue
			
        index = each_line.find(key_system)
	    
        if index != -1:
            (a, irq_num, c, irq_name) = each_line[index:].split(' ', 3)

            print(irq_num, irq_name)

            if irq_num in irq_dict:
                irq_dict[irq_num][0] += 1
            else:
                irq_dict[irq_num] = [1, irq_name[: -1]] # remove the '\n'

            continue

    f.close()

    all_irq_dict[file] = irq_dict

def search_file(path):
    for root, dirs, files in os.walk(path):
        for each in files:
            print(each)
            
            temp_str = os.path.join(root, each)
            print(temp_str)
            key_search(temp_str)

def main():
    path = get_dir()

    print(path)

    search_file(path)

    show_result()

main()
