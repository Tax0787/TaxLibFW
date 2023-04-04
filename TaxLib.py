from os import system as s
from os import getcwd as pwd
from os import chdir as cd
from sys import argv as c
pwds=pwd()
b=open(c[1]).read()
b=b.split('><')
cd(b[1])
if eval(b[3]):open('tlib_pyc.py','w').write('''from os import system as s
s('python -m compileall .')''')
def a(f:str,d:str):
    cd(pwds)
    s(f'python scripter.py {f}.x {d}')
    cd(b[1])
def m():
    cd(pwds)
    open('options.py','w').write('w=("","")')
    cd(b[1])
def p(f):
    cd(pwds)
    open('options.py','w').write(f'w=(".{f}","/{f}")')
    cd(b[1])
am=lambda f,d:(m(),a(f,d))
ap=lambda f,d:(p(f),a(f,d))
x=b[0]
if b[0]=='tm':am(b[2],b[1])
elif b[0]=='tpkg':[ap(_,b[1]) for _ in eval(b[2])]
else:
    raise TypeError(f'No TaxLib type {x}')