'''
文件夹exe病毒修复器，针对某高中而作
作者:WhitemuTeam(114)
'''
import os,winreg,re,win32api,win32con
import PySimpleGUI as sg

def checkreg():
    #检查注册表...
    #获取注册表该位置的所有键值
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
    i = 0
    while True:
        try:
            # 获取注册表对应位置的键和值
            if i==100: #防止其陷入死循环
                return None
            i += 1
            #尝试获取到文件夹exe病毒的注册表
            try:
                name=re.match(r'XP-\w*',winreg.EnumValue(key, i)[0]).group()
                return name
            except:
                pass
        except OSError:
            winreg.CloseKey(key)
            break

class removevirus:
    def __init__(self,name):
        self.name=name

    def files(self):
        os.chdir("c:\\Windows\\System32")
        name=self.name+'.EXE'
        try:
            filelist=['com.run','dp1.fne','eAPI.fne','internet.fne','krnln.fnr','og.dll','og.edt','RegEx.fnr','fne','spec.fne','ul.dll',name,'winvcreg.exe']
            for i in filelist:
                os.remove(i)
        except:
            pass
    
    def reg(self):
        name=self.name
        try:
            key = win32api.RegOpenKey(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
            win32api.RegDeleteValue(key,name)
        except:
            pass

    def main(self):
        name=self.name
        print('尝试结束文件夹exe病毒进程...')
        ml='taskkill /IM '+name+'.EXE'
        os.system(ml)
        print('删除病毒生成的文件...')
        self.files()
        print('删除病毒生成的注册表...')
        self.reg()

class checkdir:
    #检查各盘符下有没有被感染文件夹exe病毒
    def __init__(self,disk=[]):
        #获取系统下所有盘符
        for i in range(65,91):
            if i==67: #跳过C盘
                continue
            vol = chr(i) + ':'
            try:
                os.chdir(vol)
                disk.append(vol)
            except:
                pass
        self.disk=disk
    def check(self):
        #检查各盘符下有没有被感染文件夹exe病毒
        for i in self.disk:
            print('检查',i)
            os.chdir(i)
            filelist=os.listdir()
            num=0
            for a in filelist:
                num+=1
                try:
                    exename=filelist[num].split('.')
                    if exename[0]==a:
                        print('发现被感染的文件夹...正在修复...')
                        os.remove(filelist[num])
                        ml='attrib -H '+a
                        os.system(ml)
                except:
                    pass

def removeusbvirous(panpath):
    pandir=panpath+':'
    try:
        os.chdir(pandir)
    except:
        sg.popup('您的输入有误...',font=('宋体 10'),icon='LOGO.ico')
        exit()
    filelist=os.listdir()
    num=0
    for a in filelist:
        num+=1
        try:
            exename=filelist[num].split('.')
            if exename[0]==a:
                print('发现被感染的文件夹...正在修复...')
                os.remove(filelist[num])
                ml='attrib -H '+a
                os.system(ml)
        except:
            pass
    sg.popup('完成,但部分文件夹exe可能需要您手动删除',icon='LOGO.ico')

def safeusb(panpath,exepath):
    pandir=panpath+':'
    try:
        os.chdir(pandir)
    except:
        sg.popup('您的输入有误...',font=('宋体 10'),icon='LOGO.ico')
        exit()
    try:
        os.remove('autorun.inf')
    except:
        pass
    exepath1=exepath+r'\safe.exe'
    ml='copy '+exepath1+' '+pandir
    os.system(ml)
    exepath2=exepath+r'\autorun.inf'
    ml='copy '+exepath2+' '+pandir
    os.system(ml)
    os.system('attrib +H safe.exe')
    os.system('attrib +H autorun.inf')
    sg.popup('完成...',icon='LOGO.ico')
   
def main():
    name=checkreg()
    if name!=None:
        removevirus(name).main()
        checkdir().check()
        sg.popup('完成,但部分文件夹exe可能需要您手动删除',font=('楷体 15'),icon='LOGO.ico')
    else:
        sg.popup('没有在注册表检查到文件夹exe病毒，您的系统正常，但是我们也会检查在硬盘中是否存在文件夹exe病毒',font=('楷体 15'),icon='LOGO.ico')
        checkdir().check()

if __name__=='__main__':
    main()
