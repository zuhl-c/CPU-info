import psutil

# zuhl #

# number of cores
print("physical cores:", psutil.cpu_count(logical=0))
print("total cores:", psutil.cpu_count(logical=1))

# cpu frequencies
cpufreq = psutil.cpu_freq()
print(f"Max frequency: {cpufreq.max:.2f}mhz")
print(f"Min frequency: {cpufreq.min:.2f}mhz")
print(f"Current frequency: {cpufreq.current:.2f}mhz")

# cpu usage

print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=1, interval=1)):
    print(f"core {i}: {percentage}%")
print(f"Total Cpu Usage: {psutil.cpu_percent()}%")
