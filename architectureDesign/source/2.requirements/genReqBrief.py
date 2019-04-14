import requests
import json
import argparse
import os,sys
parser = argparse.ArgumentParser()
parser.add_argument("--dir",'-d',required=True,type=str)
#Get Case.json from  branch PRD
template = \
"""
用例:{title}
##################################################

{content}

"""

umlFrame=\
"""
@startuml
left to right direction

{entity}

{relation}

@enduml
"""

if __name__ == "__main__":
    args = parser.parse_args()

    if(os.path.isdir(str(args.dir))):
        r=requests.get('https://raw.githubusercontent.com/buaaembeddedse/shattuckite-doc/PRD/requirments/source/userOriented/case.json')
        with open(args.dir+'/requirements.gen.rstinc','w',encoding='utf8') as fp:
            with open(args.dir+'/case.gen.uml','w',encoding='utf8') as uml:
                entity=[]
                relation=[]
                for index,case in  enumerate(json.loads(r.text)):
                    fp.write(template.format(index=index+1,title=case['name'],content='\n'.join(case['scene'])))
                    entity.append(case['name'])
                    for user in case['user']:
                        relation.append((user,case['name']))
                uml.write(umlFrame.format(
                    entity='\n'.join(["usecase {name}".format(name = i) for i in entity]),
                    relation='\n'.join(["{user} --> {name}".format(user=user,name=name) for user,name in relation])))
            

    else:
        print("wrong dir")
        
        

