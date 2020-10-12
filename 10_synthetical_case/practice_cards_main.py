# 主文件：基于原型，负责程序的主要业务逻辑。
import practice_cards_tool as tool
"""
完成如下主要业务逻辑：
第一步：显示欢迎界面，告诉用户要输入的内容
第二步：获取用户的输入
第三步：根据用户的输入执行对应的功能操作
重复第1-3步骤
无线循环123
"""


while True:
    # 第一步：显示欢迎界面，告诉用户要输入的内容
    tool.show_menu()
    # 第二步：获取用户的输入
    cmd_num = input("请选择信息的操作：")
    # 第三步：根据用户的输入执行对应的功能操作
    if cmd_num == "1":
        tool.add_card()
    elif cmd_num == "2":
        tool.show_all()
    elif cmd_num == "3":
        tool.search_card()
    elif cmd_num == "0":
        print("退出系统")
        break
    else:
        print("输入错误，请重新输入")


