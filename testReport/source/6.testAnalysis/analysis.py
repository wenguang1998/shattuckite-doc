import json
import requests
import functools

        
requirementsObj = json.load(open('../../../requirments/source/userOriented/case.json'))
regressionObj = json.load(open('../4.testCase/regression.json','r'))





def f(x,y):
    x.extend(y)
    return x
a=functools.reduce(f,[i['cases'] for i in regressionObj],[])
b = [i['name'] for i in requirementsObj]

print(a)
print(b)


