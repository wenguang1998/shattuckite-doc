import json
import functools

entityTemplate=\
""" Table({tableName},"{tableName}\\n({verboseName})") {{ 
{content} 
    }}
"""


entity=''

with open('./uml/er.uml','w') as umlout:
    with open('./uml/er.uml.template','r') as umltemp:
        with open('./tableInfo.json','r') as jfp:
            jsobj = json.load(jfp)
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
