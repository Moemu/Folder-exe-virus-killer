# 前言

文件夹exe病毒是一种流传甚广的病毒，经常由于用户的安全性不高而导致感染

如果您观察到您的U盘/硬盘分区有下列情形的时候，那么您的U盘/硬盘分区就感染了文件夹exe病毒

![img](https://bkimg.cdn.bcebos.com/pic/4a36acaf2edda3ccc30e3f0406e93901213f9228)

你可以看到这张截图有“两个”同名的“文件夹”，但是下面的“文件夹”大小仅1,127KB，图标为WindowsXP文件夹的图标（上图截图环境为`Windows7`），类型为应用程序（文件夹不是应用程序，简单来说，文件夹没有后缀名）。由此我们得知，下面的“文件夹”（`电影.exe`）不是一个真正的文件夹。

打开假文件夹，它表面上看会打开真正的文件夹，但是实际上，它在后台偷偷下载了病毒文件并试图感染更多的文件夹，此病毒会隐藏真正的文件夹，创建一个虚拟的文件夹（传播途径，也就是假文件夹）

由于此病毒年代过于久远，看不到此病毒的源码，因此我们不知道它会不会在某一个时间点格式化您的硬盘或删除您宝贵的数据，因此，解决掉此病毒非常重要

关于这个病毒的更多信息：[文件夹EXE病毒_百度百科 (baidu.com)](https://baike.baidu.com/item/文件夹EXE病毒/263553)

2021.10.23更新：据White_mu最新研究发现，目前学校电脑上的文件夹exe病毒为**变种**版本，因此百科上内容不适用，因此我们推荐查看病毒运行详细分析：[微步在线云沙箱 (threatbook.cn)](https://s.threatbook.cn/report/file/ac4b91258b3a675af14a1674288f04512deb0c166d4f0eaa93a4b1fa24e62b3f/?env=win7_sp1_enx86_office2013)

事实上，这个病毒已经被各大杀毒软件列为危险项，杀毒软件会自动删除它，但是在没有安装杀毒软件的系统上，此类病毒非常广泛，因此，我们需要安装杀毒软件来消除此病毒

但有些时候，杀毒软件可能不会工作（比如学校电脑的冰点还原+落后的Windows Defender），让此类病毒拥有更广阔的传播空间，因此，WhitemuTeam在9个小时的努力后写出了一款程序，使其能够暂时在一定范围内撑过一段时间不被感染文件夹exe病毒

# 路径

我们发现此病毒的主程序路径为（Windows Media Player下一目录可能随机）：

```
C:\Program Files\Windows Media Player\e\b\0\3\3\9\1\4\a\b\e\3\0\2\4\2\1\1\e\5\a\d\5\9\9\3\6\9\b\6\2\b\autorun.inf\svchost.exe
```

因为某种原因，autorun.inf实际上是一个文件夹，但是被赋予了删除属性，直接打开会打开回收站，因此你需要通过以下代码查看autorun.inf中的文件（我现在把autorun.inf前的文件夹拷贝到我的U盘中了）

```powershell
G:\c>cd autorun.inf
G:\c\autorun.inf>dir
 驱动器 G 中的卷是 White_mu
 卷的序列号是 0EAF-06B4
 G:\c\autorun.inf 的目录
2021/10/21  17:57    <DIR>          ..
2011/04/22  14:08         1,148,978 svchost.exe
               1 个文件      1,148,978 字节
               1 个目录 29,763,551,232 可用字节
G:\c\autorun.inf>copy svchost.exe ..
已复制         1 个文件。
```

你可以注意到此病毒主程序为svchost.exe，如果您运行文件夹exe病毒（任何文件夹.exe），此svchost.exe就会在后台运行，但是真正的svchost.exe是系统进程，我们需要辨别哪个svchost.exe是病毒主程序来终止它的进程，打开任务管理器

找到svchost.exe，看到后面用户名一栏是不是seewo(非System)，若是，终止它的进程，若不是，那就不是病毒主程序,不用终止，而且终止前要勾选一个选项后才能终止进程，然后蓝屏:(

病毒运行详细分析：[微步在线云沙箱 (threatbook.cn)](https://s.threatbook.cn/report/file/ac4b91258b3a675af14a1674288f04512deb0c166d4f0eaa93a4b1fa24e62b3f/?env=win7_sp1_enx86_office2013)

# 使用

使用此工具的系统环境应该为Windows7 x64或以上，达不到的请使用源码编译或直接运行此工具

请注意：此工具会删除分区根目录下与文件夹同名的文件，请注意有没有珍贵文件需要备份

运行`GUI.exe`或`GUI.py`(Python环境下)

首先我们点击“清除电脑中的文件夹exe病毒”，这会读取注册表并找出病毒的主文件名并结束病毒进程，删除病毒主文件及其依赖文件（包括易语言支持库），这还会删除所有的假文件夹，显示隐藏的真文件夹

然后我们也可以“清除U盘中的文件夹exe病毒”，这个实际上和上面的选项没有太大差异，换句话来说就是自定义清除范围，如果你点了“清除电脑中的文件夹exe病毒”就不用点这里（如果你提前插入U盘的话）

上述操作完成后，部分文件夹exe病毒可能需要您手动删除，删除XP图标的文件夹exe即可

然后我们点击阻止病毒继续感染按钮，这会在病毒主程序存放的目录下（C:\Program Files\Windows Media）新建一个名为'c'的文件夹，此文件夹权限锁死，Everyone被禁止拥有此文件夹的所有权限，此时文件夹exe尝试感染电脑时就会停止工作

**请注意：点阻止病毒继续感染按钮后请不要再次使用"清除电脑中的文件夹exe病毒"，这会导致阻止功能失效！！！如果阻止功能失效，请发issus给我并附上Windows Media Player下的目录（打开显示隐藏文件功能）**

# 源码

为保证安全性，我们开源了此程序：

程序源码：`main.py`(主程序) `GUI.py`(GUI支持) `safe.py`(隐藏杀毒)

[WhitemuTeam/Folder-exe-virus-killer: 文件夹exe专杀器（针对某高中的拉跨系统制作） (github.com)](https://github.com/WhitemuTeam/Folder-exe-virus-killer)

[Folder-exe-virus-killer: 文件夹exe专杀器（针对某高中的拉跨系统制作） (gitee.com)](https://gitee.com/WhitemuTeam/Folder-exe-virus-killer)

# 吐槽

正如开源地址上面写的，某高中的系统真的是拉跨，具体表现为：

冰点还原程序没有发挥防病毒的作用（在虚拟机释放此系统wim文件，会因为冰点还原的dll文件而蓝屏）

Windows Defender没有发挥防病毒的作用（而且一个主流杀毒软件都没有）

但现在我们准备攻破冰点还原....准备给电脑装杀毒软件

# 关于

版本：v2.0

作者：White_mu(WhitemuTeam):高一，负责程序开发，文件夹exe病毒受害者

邮箱：master@muspace.top

博客：[沐の空间 - 做自己的学习笔记 (muspace.top)](https://muspace.top/)