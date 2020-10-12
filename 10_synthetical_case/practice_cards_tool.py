# 工具文件：使用函数实现具体功能
"""
*show_all():显示欢迎界面
*add_card()：新建名片
*show_all():显示名片
*search_card():查询名片
show_table_head()：show_all()和search_card()共同需要的显示的表头

deal_card():查询名片的高级功能——修改、删除、返回上一级
update_card()：deal_card()中的修改名片功能
"""

# 全局变量list
card_list = []

def show_menu():
    """
    显示欢迎界面
    :return:欢迎界面
    """
    print("*" * 50)
    print("欢迎使用【菜单管理系统】V1.0")
    print("") # 换行
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("\r") # 换行（使用换行符）
    print("0. 退出系统")
    print("*" * 50)

def add_card():
    """
    新建名片
    :return:新建名片的具体操作
    """
    print("功能：新建名片")
    # 获取用户输入信息
    name_str = input("请输入姓名：")
    phone_num=input("请输入电话：")
    qq_num=input("请输入QQ号码：")
    mail_add=input("请输入邮箱:")
    # 将上述信息分装到dict中（∵是同一个人的不同信息，若为不同人的相同信息可以使用list），方面以后使用
    card_info={"name":name_str,"phone":phone_num,"qq_num":qq_num,"mail":mail_add}
    # 保存上述dict信息到全局list中
    card_list.append(card_info)

    # 告诉用户添加名片成功
    print("添加 %s 的名片成功"%name_str) # %占位符 s字符串

def show_all():
    """
    显示全部
    :return:所有的名片信息(card_info)表
    """
    print("功能：显示全部")
    # 判断是否有名片信息
    if len(card_list) == 0:
        print("*提示：没有任何名片记录")
        return  #if满足，则函数后面不用再执行了

    # 显示的表的格式（表头)——def见下方（因search_card函数也需要该表头，所以def了）
    show_table_head()

    # 遍历全局list
    for card_info in card_list:
        # 根据显示的表的格式，读取数据
        print("%s\t\t%s\t\t%s\t\t%s"%(card_info["name"],
                                        card_info["phone"],
                                        card_info["qq_num"],
                                        card_info["mail"]))
    print("-"*50)

def show_table_head():
    """
    显示表头
    :return:表头
    """
    print("姓名\t\t电话\t\t电话\t\t邮箱")
    print("-" * 50)


def search_card():
    """
    根据姓名，查询名片
    :return:
    """
    print("功能：查询名片")
    name_str_target=input("请输入查询的姓名：")
    # 根据姓名，遍历全局list，取出每一个字典中的学生信息（比对姓名）
    for card_info in card_list:
        #判断姓名是否一致
        if name_str_target in card_info["name"]:
            #显示表头
            show_table_head()
            #显示内容
            print("%s\t\t%s\t\t%s\t\t%s" % (card_info["name"],
                                            card_info["phone"],
                                            card_info["qq_num"],
                                            card_info["mail"]))
            print("-" * 50)
            # 对名片进行一个高级处理（1.修改；2.删除；3.返回上一级）
            deal_card(card_info) ## 下面定义的函数,target_card=card_info
            break # 没有这个break就会一直打印下面这句
    else:
        print("没有找到 %s"%name_str_target)

def deal_card(target_card):
    """
    处理名片：1.修改；2.删除；3.返回上一级
    :param target_card: 上面输入的dict（个人信息）
    :return:
    """
    while True:
        # 获取用户输入
        cmd_num=input("请输入对名片的操作(提示：1-修改；2-删除；0-返回上一级)：")
        # 根据上述输入，条件判断来执行对应的操作功能
        if cmd_num == "1":
            #修改名片
            update_card(target_card)
            break
        elif cmd_num == "2":
            # 删除名片
            delete_card(target_card)
            break
        elif cmd_num == "0":
            #返回上一级
            break
        else:
            print("输入有误，请重新输入。")

def update_card(target_card):
    """
    修改名片
    :param target_card: 上面输入的dict（个人信息）
    :return:
    """

    # 获取用户输入(直接将card_info替换）
    target_card["name"]=input("请输入姓名：")
    target_card["phone"] = input("请输入电话：")
    target_card["qq_num"] = input("请输入QQ号码：")
    target_card["mail"] = input("请输入邮箱：")

    print("%s 的名片修改成功" % target_card["name"])

def delete_card(target_card):
    """
    删除名片
    :param target_card:card_info（上面输入的个人信息dict）
    :return:
    """
    card_list.remove(target_card)
    print("名片删除成功")





