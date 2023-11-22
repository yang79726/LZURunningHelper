import datetime
import time
import os

now = datetime.datetime.now().strftime("%Y-%m-%d %H").split()


def timeCompare():
    with open("C:/Users/von/Desktop/Projects/joyrun/time.txt", "r") as t:
        before = t.read()

    if before != now[0] and int(now[1]) >= 12:
        while 1:
            if netCheck():
                with open("C:/Users/von/Desktop/Projects/joyrun/time.txt", "w") as t:
                    t.write(now[0])
                return True
            else:
                time.sleep(10)
    return False


def netCheck():
    cmd = "ping www.baidu.com -n 2 >nul"
    exit_code = os.system(cmd)
    if exit_code:
        print("网络连接失败，重试中...")
        return False
    return True


if timeCompare():
    os.system("C:/Users/von/Desktop/Projects/joyrun/start.bat")
