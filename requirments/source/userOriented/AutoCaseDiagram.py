# -*- coding: UTF-8 -*-
import json

with open('.\case.json','r',encoding = 'utf-8')as f:
    json_list = json.load(f)
    # 二维数组生成
    # for i in json_list:
    #     print(type(i['name']))
        # i['prerequisites'].encode('utf-8')
    # nameCaseList = set([case['name'] for case in json_list])
    # prerequisitesList = set([case['prerequisites'] for case in json_list])
    # for i in nameCaseList:
    #     print(i)
    # print(prerequisitesList)
    exam = open(".\\uml\\example.uml","w+",encoding = 'utf-8')
    exam.write("@startuml\n")
    exam.write(":普通用户: as user\n")
    for i in json_list:
        exam.write("("+i['name']+")\n")
    for j in json_list:
        if j['prerequisites'] != []:
            for i in j['prerequisites']:
                exam.write("("+j['name']+")"+"--|>"+"("+i+")\n")
        else:
            exam.write("user"+"->"+"("+j['name']+")"+"\n")
    exam.write("@enduml\n")
    exam.close()
