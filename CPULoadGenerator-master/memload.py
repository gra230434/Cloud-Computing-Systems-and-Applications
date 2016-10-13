import sys
import getopt
import resource
import time


try:
    options, args = getopt.getopt(sys.argv[1:], "hm:d:",["help", "mem=", "time="])
    for name, value in options:
        if name in ('-h', '--help'):
            usage()
        if name in ('-m', '--mem'):
            memusage = int(value)
        if name in ('-d', '--time'):
            memtime = int(value)
except getopt.GetoptError:
    print("You can tey 'python main.py -l 20 -d 20'")

list1 = []

for j in range(3,5*memusage):
    for i in range(0,1000000):
        list1.append('abcdefg')

time.sleep( memtime )
