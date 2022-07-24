dict = {}


def showMenu():
    print("******************************")
    print("欢迎使用 【班级成绩管理系统】 V1.0")
    print("1.新增学生成绩")
    print("2.显示班级全体学生成绩")
    print("3.查询成绩")
    print("")
    print("0.退出系统")
    print("******************************")


def getSelect():
    selectNum = int(input("请输入选择的序号："))
    return selectNum


def addstuInfo():
    name = input("请输入新增的学生姓名:")
    student = input("请输入新增的学号(11位)：")
    maths = input("请输入新增的数学成绩(0-100)：")
    physics = input("请输入新增物理成绩(0-100)：")
    chemistry = input("请输入新增的化学成绩(0-100)：")
    total = int(maths) + int(physics) + int(chemistry)
    average = (int(maths) + int(physics) + int(chemistry)) / 3
    dict[name] = {"姓名": name, "学号": student, "数学": maths, "物理": physics, "化学": chemistry, "总分": total,
                  "平均分": average}
    print('添加学生\033[31m%s\033[0m成功' % dict[name]['姓名'])


def showstuInfo():
    if len(dict) == 0:
        print('数据库为空,请添加!')
    else:
        print("当前显示班级全体学生成绩：")
        print('-' * 120)
        for i in dict.items():
            print('姓名：%s\t\t学号：%s\t\t数学：%s\t\t物理：%s\t\t化学：%s\t\t总分：%s\t\t平均分：%s\t' %
                  (i[1]['姓名'], i[1]['学号'], i[1]['数学'], i[1]['物理'], i[1]['化学'], i[1]['总分'], i[1]['平均分']))
            print('-' * 120)


def querystuInfo():
    name = input("!!请输入修改的学生姓名：")
    student = input("请输入修改的学号(11位)：")
    dict[name]['学号'] = student
    maths = input("请输入修改的数学成绩(0-100)：")
    dict[name]['数学'] = maths
    physics = input("请输入修改的物理成绩(0-100)：")
    dict[name]['物理'] = physics
    chemistry = input("请输入修改的化学成绩(0-100)：")
    dict[name]['化学'] = chemistry
    total = int(maths) + int(physics) + int(chemistry)
    dict[name]['总分'] = total
    average = (int(maths) + int(physics) + int(chemistry)) / 3
    dict[name]['平均分'] = average
    print('修改成功!')


def delstuInfo():
    name = input("!!请输入删除的学生姓名：")
    dict.pop(name)
    print('删除成功!')


def seckstuInfo():
    if len(dict) == 0:
        print('数据库为空,请添加!')
    else:
        name = input("请输入要查询的姓名:")
        for i in dict.items():
            if i[1]['姓名'] == name:
                print('-' * 120)
                print('姓名：%s\t\t学号：%s\t\t数学：%s\t\t物理：%s\t\t化学：%s\t\t总分：%s\t\t平均分：%s\t' %
                      (i[1]['姓名'], i[1]['学号'], i[1]['数学'], i[1]['物理'], i[1]['化学'], i[1]['总分'], i[1]['平均分']))
                print('-' * 120)
        print('查询结束!')
        st = True
        while st:
            Modify = input('修改学生请输入\033[31m“1”\033[0m,删除学生请输入\033[31m“2”\033[0m,退出输入\033[31m“0”\033[0m:')
            if Modify == '1':
                querystuInfo()
            elif Modify == '2':
                delstuInfo()
            elif Modify == '0':
                st = False
                print('退出成功!')

static = True
while static:
    showMenu()
    num = getSelect()
    if num == 1:
        addstuInfo()
    elif num == 2:
        showstuInfo()
    elif num == 3:
        seckstuInfo()
    elif num == 0:
        print("谢谢使用本系统！")
        break
    input('--输入任意内容继续操作--')
