
def login():
    i=0
    while i <3 :
        name = input("username:")
        password = input('password:')
        name_txt=open('uname.txt','r')
        for line in name_txt.readlines():               #循环用户文件
            (uname,passwd,lock) = line.strip('\n').split()#提取用户名，密码，跟锁信息
            if uname == name:
                if lock == 'true':
                    f = 0
                    while f < 3:
                        if passwd != password:
                            if f == 2:
                                print('账号/密码错误过多，账号已被锁定，请联系管理员')
                                old = uname + ' ' + passwd + ' ' + lock + '\n'      #组合原来的用户信息
                                new_lock = 'fales'
                                new = uname + ' ' + passwd + ' ' + new_lock + '\n'  #组合新的用户信息
                                d_f = open('uname.txt', 'r')
                                d = d_f.read().replace(old, new)    #读取旧的用户信息，并替换
                                d_f.close()
                                print(d)
                                g_f = open('uname.txt', 'w+')       #以写读方式打开原有文件(如果觉得不保险，可以将老文件备份，写入新的文件中)
                                g = g_f.write(d)            #写入新的用户信息到文件
                                g_f.close()
                                name_txt.close()
                                exit(1)
                            else:
                                f += 1
                                print('账号/密码错误，还剩%s次' % (3 - f))
                                password = input('password:')       #让用户重新输入密码
                        else:
                            print('Welcom')             #登陆成功
                            name_txt.close()
                            exit(0)
                    # else:
                    #     print('账号/密码错误过多，账号已被锁定，请联系管理员')
                    #     name_txt.close()
                    #     exit(1)
                else:
                    print('账号已被锁定，请联系管理员')
                    name_txt.close()
                    exit(1)
            else:
                pass        #按行搜索用户，没有搜索到就PASS让循环继续
        else:
            i += 1
            if i == 3:
                print("账号/密码错误次数过多，已被锁定，请联系管理员")#账号不存在（防止人刷账号，所以提示为这个）
                name_txt.close()
                exit(1)
            else:
                print('账号/密码错误，还剩%s次'%(3-i))

login()