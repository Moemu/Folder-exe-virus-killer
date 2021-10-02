import time
import main

def mains():
    name=main.checkreg()
    if name!=None:
        main.removevirus(name).main()
        main.checkdir().check()
    else:
        main.checkdir().check()

times=0

while times<3:
    mains()
    time.sleep(60)
    time+=1
