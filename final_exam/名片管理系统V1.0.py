#保存的数据
dict = [{'姓名':'Tom','电话':15607879701,'邮箱':'1649823511@qq.com','地址':'美国'},
        {'姓名':'Jarry','电话':15607879702,'邮箱':'1649823512@qq.com','地址':'美国'},
        {'姓名':'利旗明','电话':15607879707,'邮箱':'1649823510@qq.com','地址':'中国'}]
#记录状态
state = True
#显示可操作内容
def showMent():
    print('-' * 40)
    print('欢迎使用【名片管理系统】V1.0')
    print('')
    print('1. 新建名片')
    print('2. 显示名片')
    print('3. 查询名片')
    print('')
    print('0. 退出系统')
    print('-' * 40)
#添加名片
def AddBusinessCard():
    name = input('请输入姓名：')
    phone = input('请输入电话：')
    mail = input('请输入邮箱：')
    address = input('请输入住址：')
    xx = {"姓名":name,"电话": phone, '邮箱': mail, '地址': address}
    dict.append(xx)
    print('------------添加成功------------')
    last = len(dict)-1
    print('添加内容为：姓名：'+dict[last]['姓名']+'  电话：'+dict[last]['电话']+'  邮箱：'+dict[last]['邮箱']+'  地址：'+dict[last]['地址'])
#显示名片
def ShowBusinessCard():
    print('')
    print('----------以下是所有名片----------')
    for i in dict:
        print('姓名：' + i['姓名'] + '\t' + '  电话：' + str(i['电话']) + '\t'
              + '  邮箱：' + str(i['邮箱']) + '\t' + '  地址：' + str(i['地址']))
        #print('姓名'+'\n'+'性别'+'\n')
    print('')
#修改名片
def ModifyBusinessCar():
    state = True
    NameState = True
    #cj = True
    #while cj:
    ModifyName = input('请输入要修改的姓名：')
    for i in dict:
        if ModifyName == i['姓名']:
            print('查询到 '+i['姓名']+' 的存在！')
            NameState = False
            while state:
                print('请进行以下内容：')
                print('【1】.姓名修改 【2】.电话修改 【3】.邮箱修改 【4】.地址修改 【0】.修改结束')
                Modify = input("输入要进行的操作：")
                if Modify == '1':
                    NewName = input('修改为：')
                    i['姓名'] = NewName
                    print('修改成功')
                elif Modify == '2':
                    Newphone = input('修改为：')
                    i['电话'] = Newphone
                    print('修改成功')
                elif Modify == '3':
                    NewMail = input('修改为：')
                    i['邮箱'] = NewMail
                    print('修改成功')
                elif Modify == '4':
                    NewAddress = input('修改为：')
                    i['地址'] = NewAddress
                    print('修改成功')
                elif Modify == '0':
                    print('----退出成功----')
                    state = False
                else:
                    print('--请输入正确的操作--')
    if NameState:
        print('没有'+ModifyName+'这个人,请添加!')
#删除名片
def DeleteBusinessCard():
    DeleteName = input('请输入要删除的名字：')
    for i in dict:
        if DeleteName == i['姓名']:
            dict.remove(i)
            print('-- '+ i['姓名']+' 已被删除成功--')
#查询名片
def QueryBusinessCard():
    state = True
    print('----------以下是操作的内容----------')
    for i in dict:
        print('姓名：' + i['姓名'] + '\t' + '  电话：' + str(i['电话']) + '\t'
              + '  邮箱：' + str(i['邮箱']) + '\t' + '  地址：' + str(i['地址']))
    print('')
    print("可进行的操作：【1】.修改名片 【2】.删除名片2 【0】.退出")
    while state:
        num = input('请输入要进行的操作：')
        if num == '1':
            ModifyBusinessCar()
            state = False
        elif num == '0':
            print('----退出成功----')
            state = False
        elif num == '2':
            DeleteBusinessCard()
            state = False
        else:
            print('请输入正确的操作!!')

while state:
    showMent()
    num = input('请输入要进行的操作：')
    if num == "1":
        AddBusinessCard()
    elif num == "2":
        ShowBusinessCard()
    elif num == "3":
        QueryBusinessCard()
    elif num == "0":
        print('----退出成功----')
        state = False
    else:
        print('请输入正确的操作!!')
    input('----输入任意内容继续操作----')