import requests
import json
import argparse
import os,sys
import hashlib
parser = argparse.ArgumentParser()
parser.add_argument("--dir",'-d',required=True,type=str)
#Get Case.json from  branch PRD
template = \
"""
用例:{title}
##################################################

{content}

"""
if __name__ == "__main__":
    args = parser.parse_args()

    if(os.path.isdir(str(args.dir))):
        r=requests.get('https://raw.githubusercontent.com/buaaembeddedse/shattuckite-doc/PRD/requirments/source/userOriented/case.json')
        with open(args.dir+'/requirements.gen.rstinc','w',encoding='utf8') as fp:
            for index,case in  enumerate(json.loads(r.text)):
                fp.write(template.format(index=index+1,
                title=case['name'],
                content='\n'.join(case['scene'])))

    else:
        print("wrong dir")
        
        

