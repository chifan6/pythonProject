# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 13:08
# @Author  : jgq
# @File    : cards_main.py
#!/usr/bin/python3
from final_exam.JiangMou import cards_tools

while True:

    cards_tools.show_menu()

    action = input("请选择操作功能：")
    print("您选择的操作是：%s" % action)

    if action in ["1", "2", "3"]:

        if action == "1":
            cards_tools.new_card()

        elif action == "2":
            cards_tools.show_all()

        elif action == "3":
            cards_tools.search_card()

    elif action == "0":
        print("已退出，欢迎再次使用【名片管理系统】")

        break
    else:
        print("输入错误，请重新输入!")

