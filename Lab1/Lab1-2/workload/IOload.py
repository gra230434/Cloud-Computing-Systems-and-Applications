import os
import sys
import time
import getopt
import subprocess
import multiprocessing


def usage():
    print(' -h help \n'
          ' -m mem loading\n'
          ' -d time\n'
          '')


def writetofile(inputsize):
    bigfile = open('bigfile','wb')
    for val in range(int(inputsize)):
        bigfile.write('00000000'*131072)
    bigfile.close()


diskusage = 0.0
disktime = 0
jobs = []

try:
    options, args = getopt.getopt(sys.argv[1:],
                                  "hi:d:", ["help", "io=", "time="])
    for name, value in options:
        if name in ('-h', '--help'):
            usage()
        if name in ('-i', '--io'):
            diskusage = float(value)
        if name in ('-d', '--time'):
            disktime = int(value)
        else:
            disktime = 20
except getopt.GetoptError:
    print("You can try 'python diskload.py -i 0.20 -d 20'")

if disktime == 0:
    disktime = 20

cmd = ['dd', 'bs=1M', 'count=256',
       'if=/dev/zero', 'of=/tmp/output', 'conv=fdatasync']
output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
diskio = output.split()
speed = diskio[13]

inputsize = float(speed) * diskusage
print("MAX wMB/s is: %s usage wMB/s is %.2f" % (speed, inputsize))
os.system("rm /tmp/output")

inputsize = (int(inputsize)+1) / 2

for i in range(disktime*2):
    millis1 = int(round(time.time() * 1000))
    the_proc = multiprocessing.Process(target = writetofile, args=((inputsize), ))
    the_proc.start()
    the_proc.join()
    millis2 = int(round(time.time() * 1000))
    throughtime = 0.5-float(float(millis2-millis1)/1000.0)
    print throughtime
    if throughtime > 0:
        time.sleep(throughtime)

os.system("rm bigfile")
