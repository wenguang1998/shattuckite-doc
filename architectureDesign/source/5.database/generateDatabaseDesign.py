import requests
import json
import argparse
import os,sys
import functools
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument("--dir",'-d',required=True,type=str)
itemTemplate=\
""" 
数据表: {verboseName}({tableName})
#####################################################

({shortHash})基本信息
++++++++++++++++++++++++++++++++++

.. table:: 数据表:{tableName} 字段信息

\t======================= ================================================== ================================================================================
\t 字段名                    字段类型                                              字段描述
\t======================= ================================================== ================================================================================
{fieldTable}\t======================= ================================================== ================================================================================

({shortHash})备注
++++++++++++++++++++++++++++++++++

{notes}

"""

tableRowTemplate =\
"""\t {key}                       {type}                                                {note}\n"""

entityTemplate=\
""" Table({tableName},"{tableName}\\n({verboseName})") {{ 
{content} 
    }}
"""


entity=''
if __name__ == "__main__":
    args = parser.parse_args()
    if not (os.path.isdir(str(args.dir))):
        print("can not find path")
        exit

    r=requests.get('https://raw.githubusercontent.com/buaaembeddedse/shattuckite-doc/PRD-dev/requirments/source/dataOriented/tableInfo.json')
    r.encoding='utf8'

    with open('./classify.table.rstinc','w') as rstout:
        jsobj = json.loads(r.text)
        relation=[]
        fileContent =  ''
        for table in jsobj:
            fieldTable=''
            for field in table['fields']:
                fieldTable+=tableRowTemplate.format(**field)
            s=hashlib.sha256()
            s.update(bytes(table['tableName'],'utf8'))
            table['notes'] = '\n'.join(table['notes'])
            fileContent += itemTemplate.format(**table,fieldTable=fieldTable,shortHash=s.hexdigest()[0:5])

        relationship = functools.reduce(lambda x,y:x+'{1:s} "0..N" --> "1" {0:s} \n'.format(*y),relation,'')
        rstout.write(fileContent)

        with open('./uml/er.uml','w') as umlout:
            with open('./uml/er.uml.template','r') as umltemp:
                relation=[]
                for table in jsobj:
                    content=''
                    for field in table['fields']:
                        if field.get('pk'):
                            content+="\tpk({key}) {type}\n".format(**field)
                        elif field.get('fk'):
                            content+="\tfk({key}) {type}\n".format(**field)
                            relation.append((field['key'],table['tableName']))
                        else:
                            content+="\t{key} {type}\n".format(**field)
                    entity+=entityTemplate.format(content=content,**table)
                relationship = functools.reduce(lambda x,y:x+'{1:s} "N" --> "1" {0:s} \n'.format(*y),relation,'')
                umlout.write(umltemp.read().format(entity=entity,relationship=relationship))