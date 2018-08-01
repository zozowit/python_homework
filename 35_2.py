import os
import os.path
import easygui as g

def get_file():
    print('get_file')
    f_path = g.fileopenbox(filetypes=['*.txt'])
    
    return f_path

def content_compare(old, new):
    if old == new:
        return True
    else:
        return False

def save_file(content, old_f):
    choice = g.buttonbox(msg='检测到内容发生变化，请选择以下操作',
                title='警告',
                choices=('覆盖保存', '放弃保存', '另存为'))

    if choice == '放弃保存':
        return
    elif choice == '覆盖保存':
        f = open(old_f, 'w')
        f.writelines(content)
        f.close()
    elif choice == '另存为':
        path = filesavebox()
        print(path)
        
        (f_dir, f_name) = os.path.split(path)

        f_new = open(path, 'w')

        f_new.writelines(content)
        f.close()

    

def welcome():
    f_content = ''
    
    b_ret = g.boolbox(msg='您是否要打开文本文件?', choices=('open', 'exit'))

    print(b_ret)
    if b_ret:
        f_path = get_file()
    print(f_path)
    if f_path is not '':
        f = open(f_path, 'r')

        
        f_content = f.readlines()

        f.close()

        (file_dir, file_name) = os.path.split(f_path)

        new_content = g.textbox(title='显示文件内容', msg='文件【%s】的内容如下：'%(file_name), text=f_content)

        ret = content_compare(f_content, new_content)

        print(ret)

        if ret is not True:
            save_file(new_content, f_path)

welcome()
