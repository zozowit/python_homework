import os
import os.path
import easygui as g

file_dict = {}

def get_file_lines(filename):
    f = open(filename, 'r', encoding='utf-8', errors='ignore')

    line_num = len(f.readlines())

    f.close()

    return line_num

def get_dir():
    path = g.diropenbox(msg='请选择您的代码库：', title='浏览文件夹')
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

    

def search_file(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            cur_path = os.path.join(root, name)
            calc_file(cur_path, name)
            print(cur_path)
            
        for name in dirs:
            print(os.path.join(root, name))

def main():
    path = get_dir()

    search_file(path)

    print(path)

main()
