# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 17:55
# @Author  : My name is Li Qiming
# @File    : 班级成绩管理系统V1.0.py

dicts = [
    {'姓名': '利旗明', '学号': '20200416006', '数学': '90', '物理': '90', '化学': '90', '总分': 270, '平均分': 90.0},
    {'姓名': '测试1', '学号': '20200416999', '数学': '99', '物理': '99', '化学': '99', '总分': 207, '平均分': 99.0},
    {'姓名': '测试2', '学号': '20200416000', '数学': '1', '物理': '11', '化学': '100', '总分': 207, '平均分': 99.0},
    {'姓名': '测试2', '学号': '202', '数学': '100', '物理': '100', '化学': '100', '总分': 207, '平均分': 99.0},
    {'姓名': '测试4', '学号': '1', '数学': '1', '物理': '1', '化学': '1', '总分': 1, '平均分': 1.0}

]


# 显示菜单
def Show():
    print('*' * 30)
    print('欢迎使用【班级成绩管理系统】V1.0')
    print('')
    print('1.新增学生成绩')
    print('2.显示班级全体学生成绩')
    print('3.查询成绩')
    print('')
    print('0.退出系统')
    print('*' * 30)


# 添加学生成绩
def Add_grades():
    Nstaic = True
    Sstaic = True
    Mstaic = True
    Pstaic = True
    Cstaic = True
    static = True
    if static:
        while Nstaic:
            Name = input('请输入学生姓名：')
            for names in dicts:
                if names['姓名'] == Name:
                    print('!学生已存在!')
                    return
                elif Name == '' or Name.isspace():
                    print('!姓名不能为空!')
                    # return
                    break
                else:
                    Nstaic = False
        while Sstaic:
            Student_number = input('请输入学生学号：')
            for ids in dicts:
                if ids['学号'] == Student_number:
                    print('!学号已存在!')
                    return
                elif Student_number == '' or Student_number.isspace():
                    print('!学号不能为空!')
                    break
                else:
                    Sstaic = False
        while Mstaic:
            Mathematics = input('请输入该学生数学成绩：')
            try:
                int(Mathematics)
                if 100 >= int(Mathematics) >= 0:
                    Mstaic = False
                else:
                    print('!请输入正确的成绩!')
            except:
                print('!请输入正确的成绩!')
        while Pstaic:
            Physics = input('请输入该学生物理成绩：')
            try:
                int(Physics)
                if 100 >= int(Physics) >= 0:
                    Pstaic = False
                else:
                    print('!请输入正确的成绩!')
            except:
                print('!请输入正确的成绩!')
        while Cstaic:
            Chemistry = input('请输入该学生化学成绩：')
            try:
                int(Chemistry)
                if 100 >= int(Chemistry) >= 0:
                    Cstaic = False
                else:
                    print('!请输入正确的成绩!')
            except:
                print('!请输入正确的成绩!')
    else:
        print('--请输入正确的内容--')
    Total_score = (int(Mathematics) + int(Physics) + int(Chemistry))
    average = round(float((int(Mathematics) + int(Physics) + int(Chemistry)) / 3), 1)
    achievement = {'姓名': Name, '学号': Student_number, '数学': Mathematics,
                   '物理': Physics, '化学': Chemistry, '总分': Total_score, '平均分': average}
    dicts.append(achievement)
    last = len(dicts) - 1
    print('已成功添加!%s!' % dicts[last]['姓名'])


# 显示全部信息
def Show_all():
    if len(dicts) == 0:
        print('数据库为空!')
        return
    else:

        for dict in dicts:
            '''print('姓名：%-5s学号：%-15s数学：%-5s物理：%-5s化学：%-5s总分：%-8s平均分：%s'
                  % (dict['姓名'], dict['学号'], dict['数学'], dict['物理'], dict['化学'], dict['总分'], dict['平均分']))'''
            '''print('姓名：{:<10}学号：{:<18}数学：{:<10}物理：{:<10}化学：{:<10}总分：{:<10}平均分：{:<10}'
                  .format(dict['姓名'], dict['学号'], dict['数学'], dict['物理'], dict['化学'], dict['总分'], dict['平均分']))'''
            print(
                '姓名：{name:<{len}}\t学号：{id:<{len1}}\t数学：{M:<{len2}}\t物理：{P:<{len3}}\t化学：{C:<{len4}}\t'
                '总分：{Z:<{len5}}\t平均分：{''Pj:<{len6}} '.format(name=dict['姓名'], id=dict['学号'], M=dict['数学'],
                                                             P=dict['物理'], C=dict['化学'], Z=dict['总分'],
                                                             Pj=dict['平均分'],
                                                             len=8 - len(dict['姓名'].encode('GBK')) + len(dict),
                                                             len1=8 - len(dict['学号'].encode('GBK')) + len(dict),
                                                             len2=8 - len(dict['数学'].encode('GBK')) + len(dict),
                                                             len3=8 - len(dict['物理'].encode('GBK')) + len(dict),
                                                             len4=8 - len(dict['化学'].encode('GBK')) + len(dict),
                                                             len5=8 - len(str(dict['总分']).encode('GBK')) + len(dict),
                                                             len6=8 - len(str(dict['平均分']).encode('GBK')) + len(dict)))

        print('*****一共有%s个学生*****' % len(dicts))


# 查询成绩
def Query_grades():
    # 显示查询到的学生信息
    def Show_one():
        print('***以下是该学生的全部信息***')
        print(
            '姓名：{name:<{len}}\t学号：{id:<{len1}}\t数学：{M:<{len2}}\t物理：{P:<{len3}}\t化学：{C:<{len4}}\t'
            '总分：{Z:<{len5}}\t平均分：{''Pj:<{len6}} '.format(name=dict['姓名'], id=dict['学号'], M=dict['数学'],
                                                         P=dict['物理'], C=dict['化学'], Z=dict['总分'],
                                                         Pj=dict['平均分'],
                                                         len=8 - len(dict['姓名'].encode('GBK')) + len(dict),
                                                         len1=8 - len(dict['学号'].encode('GBK')) + len(dict),
                                                         len2=8 - len(dict['数学'].encode('GBK')) + len(dict),
                                                         len3=8 - len(dict['物理'].encode('GBK')) + len(dict),
                                                         len4=8 - len(dict['化学'].encode('GBK')) + len(dict),
                                                         len5=8 - len(str(dict['总分']).encode('GBK')) + len(dict),
                                                         len6=8 - len(str(dict['平均分']).encode('GBK')) + len(dict)))

    # 修改查询到的学生所有信息
    def Modify_all():
        Mstaic = True
        Pstaic = True
        Cstaic = True
        while Mstaic:

            newM = input('请输入新的数学成绩：')
            if 100 >= int(newM) >= 0:
                Mstaic = False
                dict['数学'] = int(newM)
                print('!修改成功!')
            else:
                print('!请输入正确的成绩!')
        while Pstaic:

            newP = input('请输入新的物理成绩：')
            if 100 >= int(newP) >= 0:
                Pstaic = False
                dict['物理'] = newP
                print('!修改成功!')
            else:
                print('!请输入正确的成绩!')
        while Cstaic:
            newC = input('请输入新的化学成绩：')
            if 100 >= int(newC) >= 0:
                Cstaic = False
                dict['化学'] = newC
                print('!修改成功!')
            else:
                print('!请输入正确的成绩!')

    # 修改学生信息菜单
    def Modify_information():
        Mstaic = True
        Pstaic = True
        Cstaic = True
        static = True
        while static:
            Modify = input('请选择要修改的内容：\n'
                           '【1】.修改姓名 【2】.修改学号 【3】.修改数学成绩 【4】.修改物理成绩 【5】.修改化学成绩 【6】.修改所有成绩 【0】.退出\n'
                           '输入序号进行修改:')
            if Modify == '1':
                result = input('修改为：')
                dict['姓名'] = result
                print('!修改成功!')
            elif Modify == '2':
                result = input('修改为：')
                dict['学号'] = result
                print('!修改成功!')
            elif Modify == '3':
                while Mstaic:
                    result = input('修改为：')
                    if 100 >= int(result) >= 0:
                        Mstaic = False
                        dict['数学'] = result
                        print('!修改成功!')
                    else:
                        print('!请输入正确的成绩!')
                        input('')
            elif Modify == '4':
                while Pstaic:
                    result = input('修改为：')
                    if 100 >= int(result) >= 0:
                        Pstaic = False
                        dict['物理'] = result
                        print('!修改成功!')
                    else:
                        print('!请输入正确的成绩!')
            elif Modify == '5':
                while Cstaic:
                    result = input('修改为：')
                    if 100 >= int(result) >= 0:
                        Cstaic = False
                        dict['化学'] = result
                        print('!修改成功!')
                    else:
                        print('!请输入正确的成绩!')
            elif Modify == '6':
                Modify_all()
            elif Modify == '0':
                print('!退出成功!')
                return
            else:
                print('!请输入正确的序号!')
                input('--输入任意内容继续--')
            dict['总分'] = int(dict['数学']) + int(dict['物理']) + int(dict['化学'])
            dict['平均分'] = round(float((int(dict['数学']) + int(dict['物理']) + int(dict['化学'])) / 3), 1)

    if len(dicts) == 0:
        print('数据库为空!')
        return
    else:
        print('-' * 69 + '以下是可操作的信息' + '-' * 69)
        for dict in dicts:
            print(
                '姓名：{name:<{len}}\t学号：{id:<{len1}}\t数学：{M:<{len2}}\t物理：{P:<{len3}}\t化学：{C:<{len4}}\t'
                '总分：{Z:<{len5}}\t平均分：{''Pj:<{len6}} '.format(name=dict['姓名'], id=dict['学号'], M=dict['数学'],
                                                             P=dict['物理'], C=dict['化学'], Z=dict['总分'],
                                                             Pj=dict['平均分'],
                                                             len=8 - len(dict['姓名'].encode('GBK')) + len(dict),
                                                             len1=8 - len(dict['学号'].encode('GBK')) + len(dict),
                                                             len2=8 - len(dict['数学'].encode('GBK')) + len(dict),
                                                             len3=8 - len(dict['物理'].encode('GBK')) + len(dict),
                                                             len4=8 - len(dict['化学'].encode('GBK')) + len(dict),
                                                             len5=8 - len(str(dict['总分']).encode('GBK')) + len(dict),
                                                             len6=8 - len(str(dict['平均分']).encode('GBK')) + len(dict)))

        print('*****一共有%s个学生*****' % len(dicts))
    Student = input('请输入要操作的学生姓名或学号：')
    inName = True
    static1 = True
    while static1:
        for dict in dicts:
            if Student == dict['姓名'] or Student == dict['学号']:
                inName = False
                print('--查询到!%s!这个学生,你可以进行以下操作--' % dict['姓名'])
                print('【1】.显示该学生所有成绩 【2】.修改信息 【3】.删除该学生 【0】.退出')
                Serial_number = input('请输入要操作的序号：')
                if Serial_number == '1':
                    Show_one()
                    input('--输入任意内容继续--')
                elif Serial_number == '2':
                    Modify_information()
                    static1 = False
                elif Serial_number == '3':
                    dicts.remove(dict)
                    print('!%s!已被删除成功!' % dict['姓名'])
                    static1 = False
                elif Serial_number == '0':
                    print('!退出成功!')
                    static1 = False
                    return
                else:
                    print('请输入正确的序号!')
                    input('--输入任意内容继续--')
        if inName:
            print('没有!%s!这个人' % Student)
            static1 = False


static = True
while static:
    def Enter_grade():
        Show()
        information = input('请选择要进行的操作：')
        return information


    info = Enter_grade()

    if info == '1':
        Add_grades()
    elif info == '2':
        Show_all()
    elif info == '3':
        Query_grades()
    elif info == '0':
        print('----退出成功----')
        break
    else:
        print('!请输入正确的操作!')
    input('--输入任意内容继续--')
