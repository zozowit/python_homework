import os
import os.path
import easygui as g

file_dict = {}
file_dict = {}
target = 100000

def get_file_lines(filename):
    f = open(filename, 'r', encoding='utf-8', errors='ignore')

    line_num = len(f.readlines())

    f.close()

    return line_num

def get_dir():
    path = g.diropenbox(msg='请选择log位置：', title='浏览文件夹')
    return path

def calc_file(path, name):
    global file_dict
    cur_item = [0, 0]

    if (os.path.isdir(path)):
        print('is dir, just return')
        return
    
    (f_name, cur_ext) = os.path.splitext(name)
    print('cur_ext=%s, name=%s, path=%s'%(cur_ext, name, path))
    if cur_ext is not '':
        b_ret = file_dict.get(cur_ext)
        cur_line_num = get_file_lines(path)

        if b_ret is not None:
            cur_item = file_dict[cur_ext]
            cur_item[0] += 1
            cur_item[1] += cur_line_num
        else:
            cur_item[0] = 1
            cur_item[1] = cur_line_num
            
        file_dict[cur_ext] = cur_item

        print(file_dict)

def show_result():
    total_len = 0
    all_text = ''
    cur_text = ''

    global target
    
    for key in file_dict:
        cur_text = ''
        
        total_len += file_dict[key][1]
        cur_text = '【%s】源文件%d个, 源代码%d行\n'%(key, file_dict[key][0], file_dict[key][1])
        all_text += cur_text

    msg_str = '您目前共积累编写了%d行代码，完成进度：%d%%\n离%d万行代码还差%d行，请继续努力'%(total_len, total_len/target*100, target/10000, target-total_len)

    g.textbox(msg=msg_str, title='统计结果', text=all_text)    
        
def key_search(file):
    line_num = 0
    count = 0
    start = 0
    last_index = 0
    
    key_len = len(key)

    (name, ext) = os.path.splitext(file)

    if ext != '.txt':
        return
#    f = open('C:\\Python36\\test\\record.txt')
    f = open(file, encoding='gb18030', errors='ignore')

    for each_line in f:
        index = each_line.find(key, start)

        if index != -1:
            line_list.append(each_line+'\n')

    f.close()

    key_save(file, key, line_list)

def search_file():
    for root, dirs, files in os.walk(os.curdir):
        for each in files:
            print(each)
            
            temp_str = os.path.join(root, each)
            print(temp_str)
            key_search(temp_str)

def main():
    path = get_dir()

    search_file()

    print(path)

    show_result()

main()
