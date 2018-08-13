import easygui as g

msg_str = '''
【*真实姓名】为必填项
【*手机号码】为必填项
【*E-mail】为必填项
'''
field_parameter = ('*用户名', '*真实姓名', '固定电话', '*手机号码', 'QQ', '*E-mail')
value_parameter = ('','','','','','')
    
def show_multenterbox():
    ret = g.multenterbox(
        msg = msg_str,
        title = '账号中心',
        fields = field_parameter,
        values = value_parameter
        )

    print(str(ret))

    return ret

def check_input(check):
    if check['*用户名'] == '' or check['*真实姓名'] == '' or check['*手机号码'] == '' or check['*E-mail'] == '':
        return False
    else:
        return True
    
while True:
    input_dict = dict.fromkeys(field_parameter, '')
    
    ret = show_multenterbox()

    input_dict['*用户名'] = ret[0]
    input_dict['*真实姓名'] = ret[1]
    input_dict['固定电话'] = ret[2]
    input_dict['*手机号码'] = ret[3]
    input_dict['QQ'] = ret[4]
    input_dict['*E-mail'] = ret[5]
    
    print(input_dict)
    
    b_ret = check_input(input_dict)
    
    if b_ret is not True:
        g.msgbox('\'*\'项不能为空，请重新输入')
        continue
    else:
        g.textbox(msg='您的信息如下:', text=str(input_dict.values()))
        break
