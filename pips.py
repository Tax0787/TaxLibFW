from os import system as s #나중에 TPKG로 수정하시오
from os.path import dirname as dir
from os.path import basename as file
from os.path import isfile as i
from os import chdir as cd
from sys import argv as a
from urllib import request
download=lambda url,file:request.urlretrieve(url,file)
o=open
cd(dir(a[1])) #main함수 영역 1
with o(file(a[1]))as f:
    source=f.read()
    source=source.split('><')
E=type('E',(Exception,),{})
Ep=lambda x:type(x,(E,),{})
CantInstall=Ep('CantInstall')
class Pips:
    def SplitPart(self,ReTry,UseReInstall,ReTryCount,Was,RIVs):
        return
    root0=lambda self:self.install()
    root1=lambda self:self.InstallPlus()
    root2=lambda self:uninstall()or self.install()
    root3=lambda self:self.uninstall()or self.InstallPlus()
    root4=lambda self,f:self.UpdatePip()or f()
    def __init__(self,PyVer:int,pip='pip'):
        assert isinstance(pip,str),"pkg installer name must be string"
        self.__v=PyVer
        self.__x,self.__y,self.__z,self.__option=('',)*4
        self.__pip=pip
        self.GetPip_NoError=0
    def install(self):
        return s(f'{self.__x}{self.__pip}{self.y} {self__.option}install {self.__pkg}')
    def uninstall(self):
        self.__option='un'
        returns=self.install()
        self.__option=''
        return returns
    def update(self):
        self.__pkg='--upgrade '+self.__pkg
        returns=self.install()
        return returns
    def UpdatePip(self):
        self.__pkg='pip'
        returns=self.update()
        return returns
    def InstallPlus(self):
        a=self.install()
        b=self.update()
        return a or b
    def GetPip(self,NoError=0):
        if not i('get-pip.py'):download('https://bootstrap.pypa.io/get-pip.py','get-pip.py')
        a=s(f'python{self.__z} get-pip.py')
        if NoError:
            b=update('pip setuptools')
            a=a or b
            b=s(f'python{self.__z} get-pip.py')
            a=a or b
        return a
    def EzInstall(self,pips=0):
        if not i('ez_setup.py'):download('https://bootstrap.pypa.io/ez_setup.py','ez_setup.py')
        a=s(f'python{self.__z} ez_setup.py build')
        b=s(f'python{self.__z} ez_setup.py install')
        a=a or b
        if pips:b=s('easy_install pip')
        a=a or b
        return a
    def ReSetUp(self,isEZ=False,NoError=0):
        assert isinstance(isEZ,bool),"isEZ must be boolian"
        if isEZ:
            return self.EzInstall(pips=1)
        else:
            return self.GetPip(NoError=NoError)
    def RetryInstall(self,level=0):
        assert isinstance(level,int),"'ReTryLevelCode must be int"
        self.__x,self.__y,self.__z=('')*3
        match level:
            case 0:
                pass
            case 1:
                self.__y=self.__v
            case 2:
                self.__z=self.__v
            case 3:
                self.__y=self.__v
                self.__z=self.__v
            case 4:
                self.__x=f'python{self.z}'
            case 5:
                self.__y=self.__v
                self.__x=f'python{self.z}'
            case 6:
                self.__z=self.__v
                self.__x=f'python{self.z}'
            case 7:
                self.__y=self.__v
                self.__z=self.__v
                self.__x=f'python{self.z}'
            case _:
                return CantInstall("I've tried everything, but it won't install, I need to install Package Manager or change it to a special way")
        return level+1
    def Install(self,ReTry=True,UseReInstall=True,ReTryCount=0,Was=False,RIVs=None):
        assert isinstance(PyTryCount,int),"'ReTryInstall's Another Level code must be int because of the Try to Fix The Package Manager '"
        assert isinstance(Was,bool),'Was must be bool, Was mean It was "CantInstall"'
        assert isinstance(ReTry,bool),"ReTry must be boolian"
        assert isinstance(UseReInstall,bool),"UseReInstall must be boolian"
        bools=0
        if (UseReInstall and RIVs!=None:
            RIV=self.RetryInstall(level=RIVs)
        elif UseReInstall:
            RIV=self.RetryInstall()
        else:RIV=None
        if ReTry:
            #ReTry(Rootine)
            ReTryPer=ReTryCount%8
            ReTryNoPer=ReTryCount//7
            match ReTryNoPer:
                case 0:
                    a=0
                case 1:
                    a=ReSetUp()
                case 2:
                    a=ReSetUp(isEZ=True)
                case 3:
                    a=ReSetUp(NoError=1)
                case 4:
                    a=ReSetUp(isEZ=True,NoError=1)
                case _:
                    alpha=(IndexError('OutOfThe Index, maybe code>=40'),RIV)#나중에 씀 (2회 이상 쓰여서)
                    if (Error and ((not UseReInstall) or (not Was))) or ((UseReInstall or Was) and isinstance(RIV,CantInstall)):#RIV : Re Install Value, not UseReInstall - Can Error / or / UseReInstall - All Error
                        return alpha
                    else:
                        bools=1
            if not bools and not (UseReInstall or Was):
                match ReTryPer:
                    case 0:
                        b=self.root0()
                    case 1:
                        b=self.root1()
                    case 2:
                        b=self.root2()
                    case 3:
                        b=self.root3()
                    case 4:
                        b=self.root4(self.root0)
                    case 5:
                        b=self.root4(self.root1)
                    case 6:
                        b=self.root4(self.root2)
                    case 7:
                        b=self.root4(self.root3)
                    case _:
                        raise Exception('n%8 is more then 8, system error') #RealError
                a=a or b #이후 과정은 아래와 동일
            elif not bools and (UseReInstall or Was): #UseReInstall and Don't raise Error
                #Was를 이용하여 다시 여러 태스트를 함
                RIV
            elif bools and (UseReInstall or Was): #UseReInstall and eas raised Error
                #Was를 Use로, ReTryCount를 0으로,level은 그대로
                RIV
            else: #raised Error
                return alpha
        elif UseReInstall and (isinstance(RIV,CantInstall)):
                a=self.root0()
                return (a,RIV)
        else:
                return self.root0()
    def __call__(self,pkg:str,PyVer=3):
        assert isinstance(PyVer,int),"'Python Version must be int"
        self.__pkg=pkg
        self.__v=PyVer
        match 