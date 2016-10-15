import sys
import getopt
import resource
import time
from psutil import virtual_memory

def usage():
    print(' -h help \n' \
          ' -m mem loading\n' \
          ' -d time\n' \
          '')

memusage = 0.0
memtime  = 0

try:
    options, args = getopt.getopt(sys.argv[1:], "hm:d:",["help", "mem=", "time="])
    for name, value in options:
        if name in ('-h', '--help'):
            usage()
        if name in ('-m', '--mem'):
            memusage = float(value)
        if name in ('-d', '--time'):
            memtime = int(value)
except getopt.GetoptError:
    print("You can try 'python memload.py -m 20 -d 20'")

if memtime == 0:
    memtime = 20
list1 = []
unitusage = 8600000

mem = virtual_memory()
steps = int(mem.total) * memusage / unitusage

start = time.time()
for j in range(int(steps)+1):
    for i in range(0,1000000):
        list1.append('abcdefg')
end = time.time()
time.sleep( memtime-(end-start) )
