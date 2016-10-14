import os
import sys
import time
import getopt
import threading
import subprocess
import multiprocessing


class myThread (threading.Thread):
    def __init__(self, threadID, load, time):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.load = load
        self.time = time
    def run(self):
        createuserlog(self.threadID, self.load, self.time)

def createuserlog(threadID, load, time):
    command = "python CPULoadGenerator.py -l " + str(load) + " -d " + str(time) + " -c " + str(threadID)
    if os.system( command ):
        print "fail"

def usage():
    print ' -h help \n' \
          ' -l cpu loading\n' \
          ' -d time\n' \
          ''

maincpu = 0
mainmem = 0
maindisk = 0
maintime = 0

try:
    options, args = getopt.getopt(sys.argv[1:], "hl:m:i:d:",["help", "load=", "mem=", "io=","time="])
    for name, value in options:
        if name in ('-h', '--help'):
            usage()
        if name in ('-l', '--load'):
            maincpu = int(value)/100.0
        if name in ('-m', '--mem'):
            mainmem = int(value)/100.0
        if name in ('-i', '--io'):
            maindisk = int(value)/100.0
        if name in ('-d', '--time'):
            maintime = int(value)
    print("load: %.2f mem: %.2f disk: %.2f time: %d" % (maincpu, mainmem, maindisk,maintime))
except getopt.GetoptError:
    print("You can tey 'python main.py -l 20 -d 20'")

if maintime == 0:
    maintime = 1200
elif maintime <= 10:
    maintime = maintime+10

cmd1 = "-m " + str(mainmem)
cmd2 = "-d " + str(maintime)
pid = subprocess.Popen(['python', 'memload.py', cmd1, cmd2])
time.sleep( 5 )

maintime -= 5

cmd1 = "-i " + str(maindisk)
cmd2 = "-d " + str(maintime)
pid = subprocess.Popen(['python', 'diskload.py', cmd1, cmd2])
time.sleep( 5 )

maintime -= 5

thrList = [myThread(i, maincpu, maintime) for i in range(multiprocessing.cpu_count())]
for i in range(multiprocessing.cpu_count()):
    thrList[i].start()
