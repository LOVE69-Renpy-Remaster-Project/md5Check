# md5 Check By Luckykeeper
# 计算下载文件是否完整
# 日期：2022年4月28日

import ctypes,hashlib,os,re,msvcrt
from rich.console import Console
from rich.table import Table
console = Console()
# 基本参数
lv69_downdir = './'
lv69_ver10_filename_mobile=['com.love69renpyremaster.project-10-armeabi-v7a-release.apk','com.love69renpyremaster.project-10-universal-release.apk',\
                        'com.love69renpyremaster.project-100000010-arm64-v8a-release.apk','com.love69renpyremaster.project-800000010-x86_64-release.apk']
lv69_ver10_filename_pc=['LOVE69RenPyRemasterProject-1.0-mac.zip',\
                        'LOVE69RenPyRemasterProject-1.0-pc.zip']
pc_pattern="LOVE69RenPyRemasterProject"
mobile_pattern="com.love69renpyremaster.project"

# 文件MD5
lv69_ver10_mac_release_md5 = 'f4de9829afda7018c898da60e1b829c3'
lv69_ver10_pc_release_md5 = '54dd1c036c4b42b5c527b16be3e35b2e'
lv69_ver10_armv7_release_md5 = '357de705ebe0d0b6d2215b010247d0b8'
lv69_ver10_arm_universal_release_md5 = '9b0b239cb135f7b232b4579ac92c74cd'
lv69_ver10_armv8_release_md5 = '244fbb5bd11cb28ed23549ba76f7a9a3'
lv69_ver10_armx86_64_Md5_release_md5 = '51958fdbd727297f689c2675b3d27391'

# 定义变量默认值
PC_founded = False
MAC_founded = False
armv7a_founded = False
arm_universal_founded = False
armv8_founded = False
armx86_64_founded = False
# MD5 计算方法
def CheckMD5(lv69_release):
    lv69_md5 = None
    LuckyCocoa = open(lv69_release,'rb')
    md5_obj = hashlib.md5()
    md5_obj.update(LuckyCocoa.read())
    hash_code = md5_obj.hexdigest()
    LuckyCocoa.close()
    lv69_md5 = str(hash_code).lower()
    return lv69_md5
    
# 遍历文件名方法
def show_files(path, all_files):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            all_files.append(file)

    return all_files

# 程序开始

# 程序名
ctypes.windll.kernel32.SetConsoleTitleW("LOVE69 下载 MD5 校验工具 for ver1.0 \"LuckyCocoa\" By Luckykeeper , Build20220428")

console.print("[blue]_________________________________________________________[/blue]")
console.print ("LOVE69 下载 MD5 校验工具 for ver1.0 \"LuckyCocoa\" By Luckykeeper , Build20220428")
console.print("[blue]_________________________________________________________[/blue]")
console.print("""[green]

  ____          _                _          _                             
 |  _ \        | |              | |        | |                            
 | |_) |_   _  | |    _   _  ___| | ___   _| | _____  ___ _ __   ___ _ __ 
 |  _ <| | | | | |   | | | |/ __| |/ | | | | |/ / _ \/ _ | '_ \ / _ | '__|
 | |_) | |_| | | |___| |_| | (__|   <| |_| |   |  __|  __| |_) |  __| |   
 |____/ \__, | |______\__,_|\___|_|\_\\__, |_|\_\___|\___| .__/ \___|_|   
         __/ |                         __/ |             | |              
        |___/                         |___/              |_|              

[/green]""")
print("请将本程序和下载到的文件放在同一文件夹内（可以有其它文件但不要太多(会卡)），按按 Enter (回车) 键后，程序将对下载好的文件的完整性进行校验")

while True:
    if str(ord(msvcrt.getch())) == "13":
        print("请等待程序运行~")
        break

# 传入空的list接收文件名
contents = show_files(lv69_downdir, [])
for content in contents:
    # 清零 tag
    tag_pc = False
    tag_mobile = False
    # 初筛
    if re.compile(pc_pattern): #检测pc版文件
        tag_pc = True
    if re.compile(mobile_pattern):#检测移动版文件
        tag_mobile = True
    if tag_pc:
        # MAC 版
        if content == lv69_ver10_filename_pc[0]:
            
            MAC_founded = True
            MAC_filename = content

            console.print("[blue]_________________________________________________________[/blue]")
            console.print("[green]发现 MAC 1.0版文件："+content+"，开始计算 MD5 值，请稍等~[/green]")
            print("MAC 1.0版的 MD5 为：",lv69_ver10_mac_release_md5)
            down_Mac_Md5 = CheckMD5('./'+str(content))
            print("您下载文件的 MD5 值是：",down_Mac_Md5)
            if lv69_ver10_mac_release_md5 == down_Mac_Md5:
                console.print("[green]恭喜，MAC版文件完整性校验通过！Enjoy Game:)[/green]")
                console.print("[blue]_________________________________________________________[/blue]")
                MAC_result = "[green]PASSED[/green]"
            else:
                console.print("[red]MAC版文件完整性校验失败，请重新下载并再次检测文件完整性[/red]")
                console.print("[blue]_________________________________________________________[/blue]")
                MAC_result = "[red]FAILED[/red]"
        
        # PC 版
        if content == lv69_ver10_filename_pc[1]:

            PC_founded = True
            PC_filename = content

            console.print("[blue]_________________________________________________________[/blue]")
            console.print("[green]发现 PC 1.0版文件："+content+"，开始计算 MD5 值，请稍等~[/green]")
            print("PC 1.0版的 MD5 为：",lv69_ver10_pc_release_md5)
            down_PC_Md5 = CheckMD5('./'+str(content))
            print("您下载文件的 MD5 值是：",down_PC_Md5)
            if lv69_ver10_pc_release_md5 == down_PC_Md5:
                console.print("[green]恭喜，PC版文件完整性校验通过！Enjoy Game:)[/green]")
                console.print("[blue]_________________________________________________________[/blue]")
                PC_result = "[green]PASSED[/green]"
            else:
                console.print("[red]PC版文件完整性校验失败，请重新下载并再次检测文件完整性[/red]")
                console.print("[blue]_________________________________________________________[/blue]")
                PC_result = "[red]FAILED[/red]"

    if tag_mobile:
        # armv7a
        if content == lv69_ver10_filename_mobile[0]:

            armv7a_founded = True
            armv7a_filename = content

            console.print("[blue]_________________________________________________________[/blue]")
            console.print("[green]发现 armv7a 1.0版文件："+content+"，开始计算 MD5 值，请稍等~[/green]")
            print("armv7a 1.0版的 MD5 为：",lv69_ver10_armv7_release_md5)
            down_armv7a_Md5 = CheckMD5('./'+str(content))
            print("您下载文件的 MD5 值是：",down_armv7a_Md5)
            if lv69_ver10_armv7_release_md5 == down_armv7a_Md5:
                console.print("[green]恭喜，armv7a版文件完整性校验通过！Enjoy Game:)[/green]")
                console.print("[blue]_________________________________________________________[/blue]")
                armv7a_result = "[green]PASSED[/green]"
            else:
                console.print("[red]armv7a版文件完整性校验失败，请重新下载并再次检测文件完整性[/red]")
                console.print("[blue]_________________________________________________________[/blue]")
                armv7a_result = "[red]FAILED[/red]"

        # arm-universal
        if content == lv69_ver10_filename_mobile[1]:
            
            arm_universal_founded = True
            arm_universal_filename = content
            
            console.print("[blue]_________________________________________________________[/blue]")
            console.print("[green]发现 arm-universal 1.0版文件："+content+"，开始计算 MD5 值，请稍等~[/green]")
            print("arm-universal 1.0版的 MD5 为：",lv69_ver10_arm_universal_release_md5)
            down_arm_universal_Md5 = CheckMD5('./'+str(content))
            print("您下载文件的 MD5 值是：",down_arm_universal_Md5)
            if lv69_ver10_arm_universal_release_md5 == down_arm_universal_Md5:
                console.print("[green]恭喜，arm-universal版文件完整性校验通过！Enjoy Game:)[/green]")
                console.print("[blue]_________________________________________________________[/blue]")
                arm_universal_result = "[green]PASSED[/green]"
            else:
                console.print("[red]arm-universal版文件完整性校验失败，请重新下载并再次检测文件完整性[/red]")
                console.print("[blue]_________________________________________________________[/blue]")
                arm_universal_result = "[red]FAILED[/red]"

        # arm64-v8a
        if content == lv69_ver10_filename_mobile[2]:
            
            armv8_founded = True
            armv8_filename = content
            
            console.print("[blue]_________________________________________________________[/blue]")
            console.print("[green]发现 arm64-v8a 1.0版文件："+content+"，开始计算 MD5 值，请稍等~[/green]")
            print("arm64-v8a 1.0版的 MD5 为：",lv69_ver10_armv8_release_md5)
            down_armv8_Md5 = CheckMD5('./'+str(content))
            print("您下载文件的 MD5 值是：",down_armv8_Md5)
            if down_armv8_Md5 == lv69_ver10_armv8_release_md5:
                console.print("[green]恭喜，arm64-v8a版文件完整性校验通过！Enjoy Game:)[/green]")
                console.print("[blue]_________________________________________________________[/blue]")
                armv8_result = "[green]PASSED[/green]"
            else:
                console.print("[red]arm64-v8a版文件完整性校验失败，请重新下载并再次检测文件完整性[/red]")
                console.print("[blue]_________________________________________________________[/blue]")
                armv8_result = "[red]FAILED[/red]"

        # armx86_64
        if content == lv69_ver10_filename_mobile[3]:
            
            armx86_64_founded = True
            armx86_64_filename = content
            
            console.print("[blue]_________________________________________________________[/blue]")
            console.print("[green]发现 armx86_64 1.0版文件："+content+"，开始计算 MD5 值，请稍等~[/green]")
            print("armx86_64 1.0版的 MD5 为：",lv69_ver10_armv8_release_md5)
            down_armx86_64_Md5 = CheckMD5('./'+str(content))
            print("您下载文件的 MD5 值是：",down_armx86_64_Md5)
            if down_armx86_64_Md5 == lv69_ver10_armx86_64_Md5_release_md5:
                console.print("[green]恭喜，armx86_64版文件完整性校验通过！Enjoy Game:)[/green]")
                console.print("[blue]_________________________________________________________[/blue]")
                armx86_64_result = "[green]PASSED[/green]"
            else:
                console.print("[red]armx86_64版文件完整性校验失败，请重新下载并再次检测文件完整性[/red]")
                console.print("[blue]_________________________________________________________[/blue]")
                armx86_64_result = "[red]FAILED[/red]"

# 画表
reuslt_brief = Table(show_header=True, header_style="bold magenta")
reuslt_brief.add_column("文件名", style="dim", width=12)
reuslt_brief.add_column("平台")
reuslt_brief.add_column("md5", justify="center")
reuslt_brief.add_column("校验结果", justify="center")
if PC_founded:
    reuslt_brief.add_row(PC_filename,"PC（Windows and Linux）",down_PC_Md5,PC_result)
if MAC_founded:
    reuslt_brief.add_row(MAC_filename,"Mac OS",down_Mac_Md5,MAC_result)
if armv7a_founded:
    reuslt_brief.add_row(armv7a_filename,"Mobile（armv7a,Android）",down_armv7a_Md5,armv7a_result)
if arm_universal_founded:
    reuslt_brief.add_row(arm_universal_filename,"Mobile（all,Android）",down_arm_universal_Md5,arm_universal_result)
if armv8_founded:
    reuslt_brief.add_row(armv8_filename,"Mobile（armv8,Android）",down_armv8_Md5,armv8_result)
if armx86_64_founded:
    reuslt_brief.add_row(armx86_64_filename,"Mobile（x86_64,Android）",down_armx86_64_Md5,armx86_64_result)

# 总结
console.print("[yellow]以下是运行摘要：[/yellow]")

console.print(reuslt_brief)
console.print("[yellow]如果表格为空，请检查是否下载完成或检查本程序和 LOVE69 程序包放在同目录下[/yellow]")

console.print ("[green]程序运行完成!请按 Enter (回车) 键结束程序！[/green]")

while True:
    if str(ord(msvcrt.getch())) == "13":
        console.print ("[green]您已按下 Enter ,请等待程序退出![/green]")
        break