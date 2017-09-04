#!/usr/bin/env python
# -*- coding:utf-8 -*-


district_maps = {           #定义字典
    "华东区":{"山东":["济南","青岛","淄博"],"江苏":["苏州","南京","无锡"],"浙江":["杭州","宁波","温州"],},
    "华南区":{"广东":["广州","深圳","珠海"],"广西":["桂林","柳州","北海"],"海南":["三亚","海口","三沙"]},
    "华中区":{"湖北":["武汉","宜昌","黄冈"],"湖南":["长沙","株洲","湘潭"],"江西":["南昌","九江","上饶"]},
    "华北区":{"北京":["东城区","朝阳区","海淀区"],"天津":["和平区","河西区","河北区"],"河北":["石家庄","唐山","张家口"]},
    "西北区":{"宁夏":["银川","吴忠","固原"],"青海":["西宁","海东","海北藏族自治州"],"陕西":["西安","咸阳","延安"]},
    "西南区":{"四川":["成都","绵阳","广元"],"云南":["昆明","丽江","玉溪"],"贵州":["贵阳","安顺","铜仁"]},
    "东北区":{"辽宁":["沈阳","大连","鞍山"],"吉林":["长春","吉林","辽源"],"黑龙江":["哈尔滨","齐齐哈尔","牡丹江"]},
    "港澳台区":{"香港":["香港岛","九龙半岛","新界"],"澳门":["澳门半岛","离岛","路氹城"],"台湾":["台北","台中","台南"]},
}


def menu():
    now = []  # 储存当前状态
    node = []  # 储存当前地址
    for i in district_maps:
        print(i)
    node = district_maps
    now.append(node)
    t = 0
    while t < 3:
        choice = input("请输入完整的地区：")
        if len(choice) == 0:                    #判断为空时，让用户重新输入
            print("不允许输入空，请重新输入")
            continue
        if choice in node:                      #判断用户输入的地区是否在字典中
            t += 1
            if t < 2:
                t += 1
                for i in node[choice]:
                    print(i)
                now.append(node)
                node=node[choice]
            elif t == 3:                        #如果t=3代表已经到第三层目录了，打印第三层目录并让用户选择推出还是返回顶层（在第三层目录返回到第二层目录没有实现）
                for i in node[choice]:
                    print(i)
                choice = input("已打印结束，返回顶层请输入b，退出请输入q：")
                if choice == "q":
                    print("谢谢使用，再见")
                    break
                elif choice == "b":
                    if len(now) > 1:
                        t -= 1
                        for i in now[-1]:
                            print(i)
                        now.pop(-1)
                        node = now[-1]
                        continue
                else:
                    print("输入有误，谢谢使用")
                    break
        else:
            if choice== "q":
                print("谢谢使用，再见！")
                break
            elif choice=="b":
                if t == 0:
                    print("已经是最顶层")
                if len(now)>1:
                    t -= 1
                    for i in now[-1]:
                        print(i)
                    now.pop(-1)
                    node=now[-1]
            else:
                print("输入有误，请重新输入")





#简化版代码
# def menu():
#     current_layer = district_maps  # 保存当前的状态
#     last_layers = [district_maps]  # 保存之前的访问状态
#
#     while True:
#         for i in current_layer:
#             print(i)
#
#         choice = input(">>:")
#
#         if len(choice) == 0: continue
#
#         if choice in current_layer:
#             last_layers.append(current_layer)
#             current_layer = current_layer[choice]
#
#         if choice == "b":
#             if last_layers:
#                 current_layer = last_layers[-1]
#                 last_layers.pop(-1)
#         if choice == "q":
#             break

if __name__ == '__main__':
    menu()