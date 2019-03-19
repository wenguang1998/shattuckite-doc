#!/bin/python3

import json
import functools
import hashlib
template = \
'''
用例: {name}
++++++++++++++++++++++++++++++++++++++++++++++

.. table:: 用例:{name} 基本情况

    ========================== ==========================================
    用例名称                        {name}
    用例识别码                      {hash}
    参与用户                        {user}
    前提场景                        {prerequisites}
    ========================== ==========================================


.. _scene-{hash}

用例场景
###########

{scene}

.. _exception-{hash}

异常处理
############

.. table:: 用例:{name} 异常处理
{exception}


'''

def addHash(x):
    m = hashlib.sha256()
    m.update(bytes(x['name'],'utf-8'))
    x['hash']= m.hexdigest()[0:12]
    

def handlePrereq(x):
    x['prerequisites']=','.join(x['prerequisites'])
    if len(x['prerequisites'])==0:
        x['prerequisites']="无"

def handleUser(x):
    x['user']=','.join(x['user'])

def hanldleScene(x):
    x['scene'] = '\n'.join(x['scene'])

def handleEeception(x):
    header=\
'''
    ============================== =============================================== ===========================================================================
     异常描述                            异常原因                                                  异常处理
    ============================== =============================================== ===========================================================================
'''
    cellTemp=\
'''     {0}                                 {1}                                                      {2}\n'''
    if(len(x['exception']))==0:
        x['exception'] = header+cellTemp.format('无','无','无')
    else:
        x['exception'] = functools.reduce(lambda x,y:x+cellTemp.format(y[0],y[1],y[2]),x['exception'],header)

    x['exception']+=\
'''    ============================== =============================================== ==========================================================================='''



def handle(x):
    handlePrereq(x)
    handleUser(x)
    hanldleScene(x)
    handleEeception(x)
    addHash(x)

with open('./case.json','r') as ifp:
    with open('./caseGenerated.rstinc','w') as ofp:
        jsobj =[dict(i) for i in json.load(ifp)] 
        for i in jsobj:
            handle(i)

        
        ofp.write(functools.reduce(lambda x,y:x+template.format(**y),jsobj,''))


        
        

