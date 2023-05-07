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
class Pips:
    def install(self):
        return not s(f'{self.__x}pip{self.y} {self__.option}install {self.__pkg}')
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
        self.install()
        self.update()
    def GetPip(self,NoError=0):
        if not i('get-pip.py'):download('https://bootstrap.pypa.io/get-pip.py','get-pip.py')
        s(f'python{self.__z} get-pip.py')
        if NoError:
            update('pip setuptools')
            s(f'python{self.__z} get-pip.py')
    def EzInstall(self,pips=0):
        if not i('ez_setup.py'):download('https://bootstrap.pypa.io/ez_setup.py','ez_setup.py')
        s(f'python{self.__z} ez_setup.py build')
        s(f'python{self.__z} ez_setup.py install')
        if pips:s('easy_install pip')
