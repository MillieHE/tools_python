# 工具文件:  负责实现具体的功能(函数)
card_list = []  # 名片列表 包含学生信息(字典)  全局变量

def show_menu():
    """显示界面"""
    print("*" * 30)
    print("欢迎使用[名片管理系统] V1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.退出系统")
    print("*" * 30)


def add_card():
    """新建名片"""
    print("功能: 新建名片")
    # 获取用户输入
    name_str = input("请输入姓名:")
    phone_num = input("请输入电话:")
    qq_num = input("请输入qq号码:")
    mail_adr = input("请输入邮箱:")
    # 将信息封装到字典中 方便使用
    card_info = {"name": name_str, "phone": phone_num, "qq": qq_num, "mail": mail_adr}
    # 将字典添加到全局列表中保存 方便其他函数使用
    card_list.append(card_info)
    print("添加%s的名片成功" % name_str)


def show_all():
    """显示全部"""
    print("功能: 显示全部")
    # 判断是否有名片信息
    if len(card_list) == 0:
        print("提示:没有任何名片记录")
        return
    # 显示表头
    show_table_head()
    # 取出全局列表中的每一个学生信息(字典)
    for card_info in card_list:
        # 格式化操作
        print("%s\t\t%s\t\t%s\t\t%s" % (
            card_info["name"], card_info["phone"], card_info["qq"], card_info["mail"]))
    print("-" * 30)


def search_card():
    """查询名片"""
    print("功能: 查询名片")
    # 获取用户输入
    target_name = input("请输入查询的姓名:")
    # 遍历全局列表,取出每个学生信息(字典),比对姓名
    for card_info in card_list:
        # 判断姓名是否一致
        if target_name == card_info["name"]:
            # 显示表头
            show_table_head()
            print("%s\t\t%s\t\t%s\t\t%s" % (
                card_info["name"], card_info["phone"], card_info["qq"], card_info["mail"]))
            print("-" * 30)
            # 对名片进行高级处理
            deal_card(card_info)
            break
    else:
        print("没有找到%s" % target_name)


def show_table_head():
    """显示表头"""
    print("姓名\t\t电话\t\tqq\t\t邮箱")
    print("-" * 30)


def deal_card(target_card):
    """处理名片"""
    while True:
        # 获取用户输入
        cmd_num = input("请输入对名片的操作: 1.修改/ 2.删除 / 0.返回上一级")
        # 条件判断  执行不同的功能
        if cmd_num == "1":  # 修改名片
            update_card(target_card)
            break
        elif cmd_num == "2":
            delete_card(target_card)
            break
        elif cmd_num == "0":
            break
        else:
            print("输入有误,请重新输入")


def update_card(target_card):
    """修改名片"""
    # 获取用户的输入
    target_card["name"] = input("请输入姓名:")
    target_card["phone"] = input("请输入电话:")
    target_card["qq"] = input("请输入qq:")
    target_card["mail"] = input("请输入邮箱:")
    print("%s 的名片修改成功" % target_card["name"])


def delete_card(target_card):
    """删除名片"""
    card_list.remove(target_card)
    print("名片删除成功")