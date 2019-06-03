import jinja2
import hashlib
import json

def joinMultiline(x):
    if(len(x)==0):
        return '无'
    return '\n'.join(x)






ctxs = json.load(open('./regression.json','r'))
template = jinja2.Template(open('TexPreTemplate.rst.jinja2','r').read())

with open('./regression.gen.rstinc','w') as fp:
    for  ctx in ctxs:
        ctx['testType'] = "回归测试用例"

        ctx['cases'] =  joinMultiline(["+ :ref:`用例:{name}`".format(name=i) for i in ctx['cases']])
        ctx['prerequisite'] =  joinMultiline(["+ {0}".format(x) for x in ctx['prerequisite']])
        ctx['input'] =  joinMultiline(ctx['input'])
        ctx['output'] =  joinMultiline(ctx['output'])
        ctx['standard'] =  joinMultiline(ctx['standard'])
        ctx['process'] =  joinMultiline([ i.replace("\n",'') for i in ctx['process']])

        m = hashlib.sha256()
        m.update(bytes(ctx['name'],'utf-8'))
        
        ctx['hash']  =  m.hexdigest()[0:5]

        fp.write(template.render(**ctx))
