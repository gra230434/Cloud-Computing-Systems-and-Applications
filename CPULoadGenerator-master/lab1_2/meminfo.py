import time

filemem = open('/proc/meminfo')
count = 1
for line in filemem:
    if count==1:
        s1 = line
    if count==2:
        s2 = line
        break
    count += 1
filemem.close()

s1split = s1.split()
s2aplit = s2.split()

memusage = int(s1split[1]) - int(s2aplit[1])
totalemem = int(s1split[1])
usageper = 100.0 * memusage / totalemem
print("Memory Usage: %d / %d ( %.2f %% )" % (memusage, totalemem, usageper))
