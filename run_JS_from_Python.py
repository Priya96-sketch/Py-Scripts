---
#Project Name : RUN JAVASCRIPT FROM PYTHON
#Author: Priya Mondal
---
#Module Name: Js2Py --> Used to translate any valid JavaScript(ECMA Script 5.1) to Python. Acts as a Javascript Interpreter. Does not
#                       have dependencies -uses only standard python library. Translation is fully Automatic.
# LIMITATIONS OF THIS Module:
# --> Strict Mode is ignored.
# --> With statement is not supported.
# --> Indirect call to eval will be treated as direct call to eval(hence alwyas evals in local scope)

#import the necessary package
import js2py

#example 1
# A JS Command
js1 = 'console.log("Hello World!")'

res1 = js2py.eval_js(js1)

# print the result
res1
# -------------------------------------------------
# example 2
js2 = '''function add(a,b){
        return a+b;
}'''

#store the function. Taking User input
a = int(input('Enter a num: '))
res2 =js2py.eval_js(js2)

#print the result
print(res2(a,3))
