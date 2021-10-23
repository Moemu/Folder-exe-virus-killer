import  PySimpleGUI as sg
import main,os

sg.theme('Material2')
exepath=os.getcwd()

layout=[
    [sg.Button('查看电脑有没有文件夹exe病毒',font=('楷体 20'))],
    [sg.Button('清除电脑中的文件夹exe病毒',font=('楷体 20'))],
    [sg.Button('清除指定盘符中的文件夹exe病毒',font=('楷体 20'))],
    [sg.Button('阻止系统继续被感染exe病毒',font=('楷体 20'))]
]

event,value=sg.Window('文件夹exe病毒专杀器',layout=layout,icon='LOGO.ico').Read()

if event=='查看电脑有没有文件夹exe病毒':
    name=main.check()
    if name!=None:
        sg.popup('在您的电脑上发现了exe病毒',font=('楷体 15'),text_color='Red',icon='LOGO.ico')
    else:
        sg.popup('没有在注册表检查到文件夹exe病毒，您的系统正常',font=('楷体 15'),icon='LOGO.ico')

elif event=='清除电脑中的文件夹exe病毒':
    main.main()

elif event=='清除U盘中的文件夹exe病毒':
    layout=[
        [sg.Text('输入您U盘的盘符，例如：D,F,G，即一个英文字母',font=('宋体 10'))],
        [sg.Input()],
        [sg.Button('确认',font=('宋体 10'))]
    ]
    value=sg.Window(title='输入盘符',layout=layout).Read()
    panpath=value[1][0]
    main.removeusbvirous(panpath)

elif event=='阻止系统继续被感染exe病毒':
    main.safesystem() 
