import json
import jinja2
import  hashlib
TemplateStr="""

测试用例结果-{{name}} ({{hash}})
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

测试用例参见 {{ ref }}

{{ output }}

"""
ctxs = json.load(open('../4.testCase/regression.json','r'))
temp = jinja2.Template(TemplateStr)


def joinMultiline(x):
    if(len(x)==0):
        return '无'
    return '\n'.join(x)

with open('./regressionTestResult.gen.rstinc','w') as fp:
    for  ctx in ctxs:
        ctx['testType'] = "回归测试用例"

        ctx['output'] =  joinMultiline(ctx['output'])
        ctx['ref'] =  ":ref:`{testType}:{name}`".format(testType=ctx['testType'], name=ctx['name'])

        m = hashlib.sha256()
        m.update(bytes(ctx['name'],'utf-8'))
        
        ctx['hash']  =  m.hexdigest()[0:5]

        fp.write(temp.render(**ctx))


