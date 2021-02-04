# coding=utf-8
import sqlite3

conn = sqlite3.connect('d:/info.db')
curs = conn.cursor()
curs.execute("PRAGMA foreign_keys = ON")

def login_menu():
    usage = ('\tA/a: 学生登录',
             '\tB/b: 教师登录',
             '\tC/c: 管理员登录',
             '\tQ/q: 退出')
    print('Login'.center(20, '='))
    for u in usage:
        print(u)

def stu_login():
    username = input("输入账号：")
    passward = input("输入密码：")

    sql_username = 'select * from account'
    curs.execute(sql_username)
    username_list = curs.fetchall()

    target = None # 对应客户的账号密码
    for rec in username_list:
        if username in rec:
            target = rec
            break

    while True:
        if username == target[0] and passward == target[1]:
            break
        else:
            print("账号或密码错误，请重新输入。")
            username = input("输入账号：")
            passward = input("输入密码：")

def teach_login():
    username = input("输入账号：")
    passward = input("输入密码：")
    sql_username = 'select * from account'
    curs.execute(sql_username)
    username_list = curs.fetchall()

    target = None  # 对应客户的账号密码
    for rec in username_list:
        if username in rec:
            target = rec
            break

    while True:
        if username == target[0] and passward == target[1]:
            break
        else:
            print("账号或密码错误，请重新输入。")
            username = input("输入账号：")
            passward = input("输入密码：")

def admin_login():
    username = input("输入账号：")
    passward = input("输入密码：")
    sql_username = 'select * from account'
    curs.execute(sql_username)
    username_list = curs.fetchall()

    target = None  # 对应客户的账号密码
    for rec in username_list:
        if username in rec:
            target = rec
            break

    while True:
        if username == target[0] and passward == target[1]:
            break
        else:
            print("账号或密码错误，请重新输入。")
            username = input("输入账号：")
            passward = input("输入密码：")
    admin_menu()

def stu_menu():
    stu_usage = ('\tA/a: 学生信息查询',
                 '\tB/b: 学生课程信息查询',
                 '\tC/c: 奖惩信息查询',
                 '\tQ/q: 退出')
    print("学生管理界面".center(20, '='))
    for u in stu_usage:
        print(u)

def teach_menu():
    teach_usage = ('\tA/a: 学生信息管理',
                   '\tQ/q: 退出')
    print("教师管理界面".center(20, '='))
    for u in teach_usage:
        print(u)

def admin_menu():
    admin_usage = ('\tA/a: 学生信息管理',
                   '\tB/b: 学生成绩（课程）管理',
                   '\tC/c: 奖惩信息管理',
                   '\tD/d: 更改密码',
                   '\tE/e: 帮助信息',
                   '\tQ/q: 退出')
    print("管理员界面".center(20, '='))
    for u in admin_usage:
        print(u)

def manage_table_stu():
    """学生信息管理"""
    stu_usage = ('\tA/a: 查询学生信息',
                   '\tB/b: 录入学生成绩',
                   '\tC/c: 更改学生成绩',
                   '\tD/d: 删除学生成绩',
                   '\tQ/q: 退出')
    print("教师管理界面".center(20, '='))
    for u in stu_usage:
        print(u)
    while True:
        command = input('Please choose a command:')
        if command in ('A', 'a'):
            table_stu_select()
        elif command in ('B', 'b'):
            table_stu_insert()
        elif command in ('C', 'c'):
            table_stu_update()
        elif command in ('D', 'd'):
            table_stu_delete()
        elif command in ('Q', 'q'):
            break

def manage_table_stu_course():
    teach_usage = ('\tA/a: 查询学生选课信息',
                   '\tB/b: 录入学生选课信息',
                   '\tC/c: 更改学生选课信息',
                   '\tD/d: 删除学生选课信息',
                   '\tQ/q: 退出')
    print("教师管理界面".center(20, '='))
    for u in teach_usage:
        print(u)
    while True:
        command = input('Please choose a command:')
        if command in ('A', 'a'):
            table_stu_course_select()
        elif command in ('B', 'b'):
            table_stu_course_insert()
        elif command in ('C', 'c'):
            table_stu_course_update()
        elif command in ('D', 'd'):
            table_stu_course_delete()
        elif command in ('Q', 'q'):
            break

def manage_table_stu_reward_punishment():
    usage = ('\tA/a: 查询奖惩信息',
             '\tB/b: 录入奖惩信息',
             '\tC/c: 更改奖惩信息',
             '\tD/d: 删除奖惩信息',
             '\tQ/q: 退出')
    print("奖惩信息管理界面".center(20, '='))
    for u in usage:
        print(u)
    while True:
        command = input('Please choose a command:')
        if command in ('A', 'a'):
            table_stu_reward_punishment_select()
        elif command in ('B', 'b'):
            table_stu_reward_punishment_insert()
        elif command in ('C', 'c'):
            table_stu_reward_punishment_update()
        elif command in ('D', 'd'):
            table_stu_reward_punishment_delete()
        elif command in ('Q', 'q'):
            break
        else:
            print("请输入合法的选项。")
            input("按下回车以继续: ")

def table_stu_select():
    """查询学生表中指定学生的所有信息"""
    stu_id = input('请输入你的学号：')
    sql = 'select * from student where sno = %s' % (stu_id)
    curs.execute(sql)
    list = curs.fetchall()

    if not list:
        print('\tDatabase has no record at this time.')
    else:
        for rec in list:
            print(rec)
    input("按下回车以继续: ")

def table_stu_insert():
    """往student表中新增数据"""
    while True:
        sno = input('输入学号（输入0以结束）: ')
        if sno == '0':
            break
        sname = input('输入姓名: ')
        ssex = input('输入性别（男/女）: ')
        while ssex not in ('男', '女'):
            ssex = input("请输入正确的性别（男/女）：")
        sage = input('输入年龄: ')
        sclass = input('输入班级: ')
        intime = input('输入入学时间: ')
        sql = "insert into student values ('%s','%s','%s','%s','%s', '%s')" % (sno, sname, ssex, sage, sclass, intime)
        curs.execute(sql)
        conn.commit()
        print("添加成功")
        sno = None

def table_stu_update():
    while True:
        sno = input('输入需要修改信息的学生的学号（输入0以结束): ')
        if sno == '0':
            break
        print("修改开始")
        sname = input('输入姓名: ')
        ssex = input('输入性别（男/女）: ')
        while ssex not in ('男', '女'):
            ssex = input("请输入正确的性别（男/女）：")
        sage = input('输入年龄: ')
        sclass = input('输入班级: ')
        intime = input('输入入学时间: ')
        sql = """update student set 
                 sname='%s', ssex='%s', sage=%s, sclass='%s', intime='%s' 
                 where sno=%s""" % (sname, ssex, sage, sclass, intime, sno)
        curs.execute(sql)
        conn.commit()
        print("修改成功")

def table_stu_delete():
    while True:
        sno = input('输入要删除的信息对应的学号（输入0以结束）: ')
        if sno == '0':
            break
        sql = "delete from student where sno = %s" % sno
        curs.execute(sql)
        conn.commit()
        print("删除成功")

def table_stu_course_select():
    stu_id = input('请输入你的学号：')
    sql = 'select cname from course where cno in (select cno from stu_course where sno = %s)' % (stu_id)
    curs.execute(sql)
    list = curs.fetchall()

    if not list:
        print('暂无此记录')
        input("按下回车以继续: ")
    else:
        for rec in list:
            print(rec)
    input("按下回车以继续: ")

def table_stu_course_insert():
    while True:
        sno = input('输入学号（输入0以结束）: ')
        if sno == '0':
            break
        cno = input("输入要选修的课程号")
        list = table_course_select()
        cno_list = []
        for rec in list:
            cno_list.append(rec[0])

        while cno not in cno_list:
            cno = input("没有这门课，请输入正确的课程编号（输入“q”以退出）：")
            if cno == 'q':
                break

        grade = input("输入这位学生该门课程的成绩（若暂无，请输入”n“）：")
        if grade == 'n':
            grade = ''

        sql = "insert into stu_course(sno, cno, grade) values ('%s','%s','%s')" % (
        sno, cno, grade)
        curs.execute(sql)
        conn.commit()
        print("添加成功")

def table_stu_course_update():
    while True:
        sno = input('输入需要修改信息的学生的学号（输入0以结束): ')
        if sno == '0':
            break
        cno = input('输入该学生所选的课程编号: ')
        print("修改开始")
        grade = input("输入该学生该门课成绩（若暂无，请输入”n“）：")
        if grade == 'n':
            grade = ''
        sql = """update stu_course set grade=%s 
                 where sno='%s' and cno='%s'""" % (grade, sno, cno)
        curs.execute(sql)
        conn.commit()
        print("修改成功")

def table_stu_course_delete():
    while True:
        sno = input('输入要删除的学生对应的学号（输入0以结束）: ')
        if sno == '0':
            break
        cno = input('输入该学生所选的课程编号: ')
        sql = "delete from stu_course where sno = '%s' and cno = '%s'" % (sno, cno)
        curs.execute(sql)
        conn.commit()
        print("删除成功")

def table_stu_reward_punishment_select():
    stu_id = input('请输入学号：')
    sql = 'select * from stu_reward_punishment where sno = %s' % (stu_id)
    curs.execute(sql)
    list = curs.fetchall()

    if not list:
        print('该学生暂无奖惩记录')
        input("按下回车以继续: ")
    else:
        reward = []
        punishment = []
        for rec in list:
            if rec[2] != None:
                reward.append(rec[2])
            if rec[3] != None:
                punishment.append(rec[3])
    if reward:
        print('奖项: ', reward)
    if punishment:
        print('惩罚: ', punishment)
    input("按下回车回到管理界面: ")

def table_stu_reward_punishment_insert():
    while True:
        sno = input('输入学号（输入0以结束）: ')
        if sno == '0':
            break
        reward = input("请输入该学生的奖励信息（若无，请输入”n“）：")
        punishment = input("请输入该学生的惩罚信息（若无，请输入”n“）：")
        if reward == 'n':
            reward = ''
        if punishment == 'n':
            punishment = ''
        sql = "insert into stu_reward_punishment(sno, reward, punishment) values ('%s','%s','%s')" % (sno, reward, punishment)
        curs.execute(sql)
        conn.commit()
        print("添加成功")

def table_stu_reward_punishment_update():
    while True:
        sno = input('输入需要修改信息的学生的学号（输入0以结束): ')
        if sno == '0':
            break
        print("修改开始")
        reward = input("请输入该学生的奖励信息（若无，请输入”n“）：")
        punishment = input("请输入该学生的惩罚信息（若无，请输入”n“）：")
        if reward == 'n':
            reward = ''
        if punishment == 'n':
            punishment = ''
        sql = """update stu_reward_punishment set 
                 reward = '%s', punishment = '%s'
                 where sno = '%s'""" % (reward, punishment, sno)
        curs.execute(sql)
        conn.commit()
        print("修改成功")

def table_stu_reward_punishment_delete():
    while True:
        sno = input('输入要删除的信息对应的学号（输入0以结束）: ')
        if sno == '0':
            break
        flag = input("请输入要删除奖励（输入”1“）还是惩罚（输入”2“）？: ")
        if flag == '1':
            sql = "delete from stu_reward_punishment where reward is not null and sno = %s" % sno
        if flag == '2':
            sql = "delete from stu_reward_punishment where punishment is not null and sno = %s" % sno
        else:
            while flag not in ('1', '2'):
                flag = input("请输入合法的选项：")
        curs.execute(sql)
        conn.commit()
        print("删除成功")

def table_course_select():
    sql = 'select * from course'
    curs.execute(sql)
    list = curs.fetchall()

    return list

def table_account_update():
    while True:
        username = input('输入需要修改的账号（输入0以结束): ')
        if username == '0':
            break
        print("修改开始")
        passward = input('输入新密码: ')
        sql = """update account set passward=%s 
                 where username='%s'""" % (passward, username)
        curs.execute(sql)
        conn.commit()
        print("修改成功")

def update_passward():
    while True:
        usage = ('\tA/a: 修改密码',
                 '\tQ/q: 退出')
        print("更改密码".center(20, '='))
        for u in usage:
            print(u)
        command = input('Please choose a command:')
        if command in ('A', 'a'):
            table_account_update()
            input("按下回车回到管理界面: ")
        elif command in ('Q', 'q'):
            break
        else:
            print("请输入合法的选项。")
            input("按下回车以继续: ")

def main():
    while True:
        login_menu() # 运行登录界面
        command = input('Please choose a command:')
        if command in ('A', 'a'):
            """以学生身份登录"""
            stu_login()
            while True:
                stu_menu()
                command1 = input('Please choose a command:')
                if command1 in ('A', 'a'):
                    table_stu_select()
                elif command1 in ('B', 'b'):
                    table_stu_course_select()
                elif command1 in ('C', 'c'):
                    table_stu_reward_punishment_select()
                elif command1 in ('Q', 'q'):
                    break
                else:
                    print("请输入合法的选项。")
                    input("按下回车以继续: ")
        elif command in ('B', 'b'):
            teach_login()
            while True:
                teach_menu()
                command4 = input('Please choose a command:')
                if command4 in ('A', 'a'):
                    manage_table_stu()
                elif command4 in ('Q', 'q'):
                    break
                else:
                    print("请输入合法的选项。")
                    input("按下回车以继续: ")
        elif command in ('C', 'c'):
            admin_login()
            while True:
                command2 = input('Please choose a command:')
                if command2 in ('A', 'a'):
                    manage_table_stu()
                elif command2 in ('B', 'b'):
                    manage_table_stu_course()
                elif command2 in ('C', 'c'):
                    manage_table_stu_reward_punishment()
                elif command2 in ('D', 'd'):
                    update_passward()
                elif command2 in ('E', 'e'):
                    print("暂无帮助信息。")
                elif command2 in ('Q', 'q'):
                    break
                else:
                    print("请输入合法的选项。")
                    input("按下回车以继续: ")
        elif command in ('Q', 'q'):
            print("感谢使用，再见。")
            break
        else:
            print("请输入合法的选项。")
            input("按下回车以继续: ")

main()