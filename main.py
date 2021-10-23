'''
文件夹exe病毒移除器，针对某高中而作
作者:WhitemuTeam(114)
'''
import os,re
import PySimpleGUI as sg

def check():
    #2021.10.23更新：我们发现学校运行的是与百度百科不同的版本，于是我们更换检查策略
    #检查C:\Program Files\Windows Media Player
    try:
        filelist=os.listdir('C:\Program Files\Windows Media Player')
    except:
        sg.popup('您的系统正常，没有发现文件夹exe病毒',icon='LOGO.ico')
    for filename in filelist:
        if len(filename)==1:
            return filename
    sg.popup('您的系统正常，没有发现文件夹exe病毒',icon='LOGO.ico')

class removevirus:
    def __init__(self,name):
        self.name=name

    def files(self):
        try:
            os.chdir('C:\Program Files\Windows Media Player')
            ml='takeown /f '+self.name+' /r /A /D Y'
            os.system(ml)
            ml='rd '+self.name+' /s /q'
            os.system(ml)
            os.system('del %HOMEPATH%\AppData\Local\Temp\*')
        except:
            pass

    def main(self):
        print('尝试结束文件夹exe病毒进程...')
        print('获取到进程')
        ml='tasklist >list.txt'
        os.system(ml)
        print('分析进程')
        with open('list.txt','r') as f:
            tasklist=f.readlines()
        for task in tasklist:
            if re.match(r'svchost.exe\s+\d+\s+Console',task)!=None:
                taskline=re.match(r'svchost.exe\s+\d+\s+Console',task).group()
                pid=re.search('\d+',taskline).group()
                break
        try:
            ml='taskkill /PID '+pid+' /F'
            print('检测到病毒进程...')
            os.system(ml)
        except:
            print('无病毒进程...')
        os.remove('list.txt')
        print('删除病毒生成的文件...')
        self.files()

class checkdir:
    #检查各盘符下有没有被感染文件夹exe病毒
    def __init__(self,disk=[]):
        #获取系统下所有盘符
        for i in range(65,91):
            vol = chr(i) + ':\\'
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
                otherexe=a+'.exe'
                if otherexe in filelist:
                    print('发现',a,'被感染...正在修复...')
                    try:
                        os.remove(otherexe)
                    except:
                        pass
                    ml='attrib -H '+'"'+a+'"'
                    os.system(ml)
                num+=1
            if os.path.isdir('autorun.inf'):
                os.system('takeown /f autorun.inf /r /A /D Y')
                os.system('rd /S /Q autorun.inf')

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

def safesystem():
    sg.popup('请在接下来出现的命令提示符中输入Y')
    os.chdir('C:\Program Files\Windows Media Player')
    os.mkdir('c')
    os.system('cacls c /D Everyone')
    sg.popup('完成...',icon='LOGO.ico')
   
def main():
    filename=check()
    if filename!=None:
        removevirus(filename).main()
        checkdir().check()
        sg.popup('完成,但部分文件夹exe可能需要您手动删除',font=('楷体 15'),icon='LOGO.ico')
    else:
        sg.popup('没有在Media Player文件夹中检查到文件夹exe病毒主程序，您的系统正常，但我们也会清除在硬盘中的任何文件夹exe病毒',font=('楷体 15'),icon='LOGO.ico')
        checkdir().check()

if __name__=='__main__':
    main()
