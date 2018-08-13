import os
import os.path
import easygui as g

all_irq_dict = {}

def get_dir():
    path = g.diropenbox(msg='请选择log所在文件夹：', title='浏览文件夹')
	
    print('get_dir', path)
    return path

def show_result():
    all_text = ''
    cur_text = ''
    cur_statistic= ''

    
    for key in file_dict:
        cur_text = ''
        value = file_dict[key]
        
        cur_text = '文件名：' + key +'\n'
        for each in value:
            cur_text += 'IRQ[%s]: %d times\n'%(each + value[each])
            
        all_text += cur_text

    g.textbox(msg=msg_str, title='统计结果', text=all_text)    
        
def key_search(file):
    irq_dict = {}

    key_gic = ''
    key_system = ''
    
    (name, ext) = os.path.splitext(file)

    if ext != '.txt':
        return

    f = open(file, encoding='gb18030', errors='ignore')

    for each_line in f:
        index = each_line.find(key_gic)

        if index != -1:
            (a, b, c) = each_line[index:].split(' ', 2)
			
        index = each_line.find(key_system)
	    
        if index != -1:
            (a, b, c) = each_line[index:].split(' ', 2)

        if b in irq_dict:
            irq_dict[b] += 1
        else:
            irq_dict[b] = 1

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
