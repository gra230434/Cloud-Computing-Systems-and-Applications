import time


filecpu = open("/proc/stat")
count = 1
for line in filecpu:
    if count==1:
        first = line
        break
    count += 1
file.close()

time.sleep(1)

file = open("/proc/stat")
count = 1
for line in file:
    if count==1:
        second = line
    count += 1
file.close()

firstlist = first.split()
secondlist = second.split()

s1 = 0.0
s2 = 0.0
for val in range(1,len(firstlist)):
    s1 = s1 + int(firstlist[val])
    s2 = s2 + int(secondlist[val])

totaltime = 0.0
totalide = 0.0
totaltime = s2 - s1
totalide = int(secondlist[4])-int(firstlist[4])
answer = 100 * (totaltime - totalide) / totaltime
print("CPU Loading: %.3f" % (answer))
