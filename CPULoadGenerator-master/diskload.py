import os
import time
import subprocess

def usage():
    print ' -h help \n' \
          ' -m mem loading\n' \
          ' -d time\n' \
          ''

try:
    options, args = getopt.getopt(sys.argv[1:], "hi:d:",["help", "io=", "time="])
    for name, value in options:
        if name in ('-h', '--help'):
            usage()
        if name in ('-i', '--io'):
            diskusage = float(value)
        if name in ('-d', '--time'):
            disktime = int(value)
except getopt.GetoptError:
    print("You can try 'python diskload.py -i 0.20 -d 20'")

cmd = ['dd', 'bs=1M', 'count=256', 'if=/dev/zero', 'of=/tmp/output', 'conv=fdatasync']
output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
diskio = output.split()
speed = diskio[13]

inputsize = int(speed) * diskusage
inputsize = int(inputsize)

os.system("rm /tmp/output")

with open('bigfile', 'wb') as bigfile:
    for i in range(disktime*2):
        millis1 = int(round(time.time() * 1000))
        bigfile.write('0'*inputsize*1048575)
        millis2 = int(round(time.time() * 1000))
        time.sleep(0.5-((millis2-millis1)/1000))

os.system("rm bigfile")
