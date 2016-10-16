import time
import curses

stdtscr = curses.initscr()
cpuinfo_pre = []
disk_pre = []


def display_info(string, x, y):
    global stdtscr
    stdtscr.addstr(y, x, string, curses.color_pair(0))
    stdtscr.refresh()


def set_screen():
    global stdtscr
    stdtscr.clear()
    stdtscr.border(0)
    curses.start_color()


def cpuinfo():
    global cpuinfo_pre
    filecpu = open("/proc/stat")
    count = 1
    for line in filecpu:
        if count == 1:
            cpuinfo = line
            break
            count += 1
    filecpu.close()
    if len(cpuinfo_pre) == 0:
        cpuinfo_pre = cpuinfo.split()
    else:
        cpuinfo_now = cpuinfo.split()
        s1 = 0.0
        s2 = 0.0
        for val in range(1, len(cpuinfo_pre)):
            s1 = s1 + int(cpuinfo_pre[val])
            s2 = s2 + int(cpuinfo_now[val])
        totaltime = 0.0
        totalide = 0.0
        totaltime = s2 - s1
        totalide = int(cpuinfo_now[4])-int(cpuinfo_pre[4])
        answer = 100 * (totaltime - totalide) / totaltime
        cpuinfo_pre = cpuinfo_now
        return "CPU Loading: %.3f" % (answer)


def meminfo():
    filemem = open('/proc/meminfo')
    count = 1
    for line in filemem:
        if count == 1:
            s1 = line
        if count == 2:
            s2 = line
            break
        count += 1
    filemem.close()
    s1split = s1.split()
    s2aplit = s2.split()
    memusage = int(s1split[1]) - int(s2aplit[1])
    totalemem = int(s1split[1])
    usageper = 100.0 * memusage / totalemem
    return "Memory Usage: %d / %d ( %.2f %% )" \
           % (memusage, totalemem, usageper)


def diskinfo(val=0):
    global disk_pre
    disk_now = []
    filedisk = open('/proc/diskstats')
    for line in filedisk:
        tmpdisk = line.split()
        if tmpdisk[0] == '8':
            if len(filter(str.isdigit, tmpdisk[2])) == 0:
                disk_now.append(tmpdisk)
    if len(disk_pre) == 0 and val == 0:
        disk_pre = disk_now
    else:
        val = int(val)
        readspeed = (int(disk_now[val][5]) - int(disk_pre[val][5])) \
            / 2.0 / 1024.0
        writespeed = (int(disk_now[val][9]) - int(disk_pre[val][9])) \
            / 2.0 / 1024.0
        disk_pre = disk_now
        return "%s Disk Read speed is %.3f MB/s, Write Speed is %.3f MB/s" \
               % (disk_now[val][2], readspeed, writespeed)


if __name__ == '__main__':
    try:
        set_screen()
        display_info('Welcome to Top by Kevin', 0, 0)
        cpuinfo()
        diskinfo()
        time.sleep(1)
        while True:
            display_info(cpuinfo(), 1, 3)
            display_info(meminfo(), 1, 5)
            for val in range(len(disk_pre)):
                display_info(diskinfo(val), 1, 7+val)
            stdtscr.refresh()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        curses.endwin()
