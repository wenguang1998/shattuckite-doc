import os
import json
with open('./case.json','r') as fp: 
    jsobj=json.load(fp)
    nameCaseList = set([case['name'] for case in jsobj])
    umlList = set([i.split('.')[0] for i in os.listdir('./uml')])
    print(nameCaseList-umlList)

    