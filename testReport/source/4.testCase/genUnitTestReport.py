import jinja2
import hashlib
import json

def joinMultiline(x):
    if(len(x)==0):
        return '无'
    return '\n'.join(x)

ctxs = json.load(open('./unittest.json','r'))
template = jinja2.Template(open('TexPreTemplate.rst.jinja2','r').read())

with open('./unittest.gen.rstinc','w') as fp:
    for  ctx in ctxs:
        ctx['testType'] = "单元测试用例"
        ctx['cases'] =  joinMultiline(ctx['cases'])

        if ctx['prerequisite'] == "RESTFUL_TEST_PRE":
            ctx['prerequisite'] = ["+ 关系型数据库部署","+ RESTFul服务器部署"]

        ctx['prerequisite'] =  joinMultiline(ctx['prerequisite'])

        ctx['input'] =  joinMultiline(ctx['input'])

        if ctx['output'] == "RESTFUL_TEST_OUTPUT":
            ctx['output'] = ["通过或不通过"]
        ctx['output'] =  joinMultiline(ctx['output'])

        ctx['standard'] =  joinMultiline(ctx['standard'])

        if ctx['process'] ==  "UNITTES_DEFAULT_PROCESS" :
            ctx['process'] = ["1. 建立临时测试数据库",
            "2. 创建测试用临时数据",
            "3. 调用接口，并检查返回是否为期望结果",
            "4. 销毁测试数据库"
            ]

        ctx['process'] =  joinMultiline(ctx['process'])

        m = hashlib.sha256()
        m.update(bytes(ctx['name'],'utf-8'))
        
        ctx['hash']  =  m.hexdigest()[0:5]

        fp.write(template.render(**ctx))
