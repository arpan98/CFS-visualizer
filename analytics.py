import matplotlib.pyplot as plt

n = 5

truntimes = []
cpu_times = []

cur_time = 0
cur_proc_index = -1

for x in xrange(0,n):
    truntimes.append([])

with open('results.txt', 'r') as file:
    for line in file:
        if line.startswith("CPU Time"):
            cur_time = int(line[11:])
            cpu_times.append(cur_time)

        if line.startswith("Adding"):
            proc_name = line[7:8]
            index = ord(proc_name) - ord('A')
            vrt = int(line[23:])
            if len(truntimes[index]) <= cur_time:
                truntimes[index].append(vrt)
            else:
                truntimes[index][cur_time] = vrt

        if line.startswith("Removing"):
            proc_name = line[9:10]
            index = ord(proc_name) - ord('A')
            cur_proc_index = index
            vrt = int(line[25:])
            if len(truntimes[index]) <= cur_time:
                truntimes[index].append(vrt)
            else:
                truntimes[index][cur_time] = vrt

        if line.startswith("Inserting"):
            proc_name = line[10:11]
            index = ord(proc_name) - ord('A')
            vrt = int(line[26:])
            if len(truntimes[index]) <= cur_time:
                truntimes[index].append(vrt)
            else:
                truntimes[index][cur_time] = vrt

        for x in xrange(0,n):
            if len(truntimes[x]) != cur_time + 1:
                if len(truntimes[x]) == 0:
                    truntimes[x].append(0);
                if cur_proc_index == x and cur_proc_index != -1:
                    # Increase truntime by 1
                    truntimes[x].append(truntimes[x][cur_time-1] + 1)
                elif cur_proc_index != x and cur_proc_index != -1:
                    # Copy same truntime
                    truntimes[x].append(truntimes[x][cur_time-1])

print truntimes

for x in xrange(0,n):
    plt.plot(cpu_times, truntimes[x], label=str(unichr(x+65)))

plt.legend(loc='upper left')
plt.xlabel('CPU Time')
plt.ylabel('Total Virtual Runtime')
plt.show()
    