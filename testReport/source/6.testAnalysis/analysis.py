import json
import requests
import functools
import hashlib

        
requirementsObj = json.load(open('../../../requirments/source/userOriented/case.json'))
regressionObj = json.load(open('../4.testCase/regression.json','r'))
unittestObj = json.load(open('../4.testCase/unittest.json','r'))





def f(x,y):
    x.extend(y)
    return x
a=functools.reduce(f,[i['cases'] for i in regressionObj],[])
b = [i['name'] for i in requirementsObj]



# print(len(a))
# print(b)
# print(len(b))
# print(len(unittestObj))
# print(len(regressionObj))



ctxs=regressionObj
template="+ :ref:`{testType}:{name}`: {cases}"


with open('./uncorvered.gen.rstinc','w') as fp:
    uncov = (set(b)-set(a))
    fp.write("\n".join(
        ["+ :ref:`用例:{name}`".format(name=i) for i in uncov]
        
        ))




with open('./RegressionCases.gen.rstinc','w') as fp:
    for  ctx in ctxs:
        ctx['testType'] = "回归测试用例"

        ctx['cases'] =" , ".join([":ref:`用例:{name}`".format(name=i) for i in ctx['cases']])
        m = hashlib.sha256()
        m.update(bytes(ctx['name'],'utf-8'))
        
        ctx['hash']  =  m.hexdigest()[0:5]

        fp.write(template.format(**ctx))
        fp.write("\n")