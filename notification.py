# Script made for Polish Minecraft servers using essentials msg plugin

import playsound
import time

pathToMinecraft = "<path to .minecraft folder>"
nick = "<your nickname>"
prefix = "<your prefix (ex. VIP) | leave empty if none>"

flogi = open("msg_log.txt", "w")
flogi.close()


def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


if __name__ == "__main__":
    logfile = open(pathToMinecraft+"/logs/latest.log", "r")
    loglines = follow(logfile)
    for line in loglines:
        if "[main/INFO]: [CHAT]" in line and "-> Ja]" in line or "[main/INFO]: [CHAT]" in line and nick in line and not prefix+" "+nick in line:
            playsound.playsound("pop.mp3")
            flogi = open("msg_log.txt", "a")
            flogi.write(line)
            flogi.close()
        if "off" in line and prefix+" "+nick in line:
            break
