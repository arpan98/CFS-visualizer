import matplotlib.pyplot as plt

n = 5

truntimes = []
cpu_times = []

last_run = -1

for x in xrange(0,n):
    truntimes.append([])

with open('results.txt', 'r') as file:
    for line in file:
        curTime = int(line.split(' ')[0])
        cpu_times.append(curTime)
        print line.split(':')[1].strip()[:11]
        if len(line.split(':')[1].strip()) > 0:
            if line.split(':')[1].strip().endswith(', Completed'):
                last_run = ord(line.split(':')[1].strip()[:-11]) - ord('A')
            else:
                last_run = ord(line.split(':')[1].strip()) - ord('A')
        
        for x in xrange(0, n):
            if last_run == -1:
                truntimes[x].append(0)
            elif last_run == x:
                truntimes[x].append(truntimes[x][curTime-1] + 1)
            else:
                truntimes[x].append(truntimes[x][curTime-1])

print truntimes

for x in xrange(0,n):
    plt.plot(cpu_times, truntimes[x], label=str(unichr(x+65)))

plt.legend(loc='upper left')
plt.xlabel('CPU Time')
plt.ylabel('Total Runtime')
plt.show()