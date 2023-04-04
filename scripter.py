from sys import argv as a
from os import mkdir as d
from os import chdir as cd
from os.path import isdir as e
from options import w
cd(a[2])
def dirs():
    if not e('pkg'):d('pkg')
z=a[1].split('.')[0]
x,y=w
y='pkg'+y
s=open(z+'.pkg').read()
c=''
def r(a:str,b:str):
    global c
    c=c.replace(a,b)
b=''
for _ in s.split('\n'):
    c=_
    a=c.split('=')
    print(a)
    c=a[1]+'>a<'+a[0]
    r(',','>i<')
    c='$f '+c
    r('>i<',' $i ')
    r('>a<',' $a ')
    r('$f','from')
    r('$i','import')
    r('$a','as')
    r('/','\\')
    r('\\','.')
    b+=c+'\n'
if w!=('',''):dirs()
open(y+'.py','w').write(b)
b=f'from pkg{x} import *\n'
b+=open(z+'.scripter').read().replace('main:','def main():')
b+='\nif __name__=="__main__":main()'
open(z+'.py','w').write(b)