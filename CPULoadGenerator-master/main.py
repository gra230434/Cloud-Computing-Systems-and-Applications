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
maintime = 0

try:
    options, args = getopt.getopt(sys.argv[1:], "hl:m:d:",["help", "load=", "mem=", "time="])
    for name, value in options:
        if name in ('-h', '--help'):
            usage()
        if name in ('-l', '--load'):
            maincpu = int(value)/100.0
        if name in ('-m', '--mem'):
            mainmem = int(value)
        if name in ('-d', '--time'):
            maintime = int(value)
    print("load: %f time: %d" % (maincpu, maintime))
except getopt.GetoptError:
    print("You can tey 'python main.py -l 20 -d 20'")

cmd1 = "-m " + str(mainmem)
cmd2 = "-d " + str(maintime)
pid = subprocess.Popen(['python', 'memload.py', cmd1, cmd2])

time.sleep( 5 )

thrList = [myThread(i, maincpu, maintime) for i in range(multiprocessing.cpu_count())]
for i in range(multiprocessing.cpu_count()):
    thrList[i].start()
