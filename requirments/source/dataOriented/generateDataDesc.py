import json
import functools
import hashlib

itemTemplate=\
""" 

数据表: {verboseName}({tableName})
#####################################################

({shortHash})基本信息
++++++++++++++++++++++++++++++++++

.. table:: 数据表:{tableName} 字段信息

    ======================= ================================================== ================================================================================
    字段名                    字段类型                                              字段描述
    ======================= ================================================== ================================================================================
    {fieldTable}
    ======================= ================================================== ================================================================================



({shortHash})备注
++++++++++++++++++++++++++++++++++

{notes}

"""

tableRowTemplate =\
"""    {key}                       {type}                                                {note}\n"""


with open('./classify.table.rstinc','w') as rstout:
        with open('./tableInfo.json','r') as jfp:
            jsobj = json.load(jfp)
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
            
