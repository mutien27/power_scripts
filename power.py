#!/usr/bin/python -O

import sys
import re

CYCLE_TIME = float(1) / 667000000 # s

#workload = sys.argv[1]
#fout_name = sys.argv[2]

pattern = re.compile("([0-9]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)")

# === initialization ===
total_cycle = 0
energy = 0 # mJ
background_energy = 0 # mJ
actpre_energy = 0 # mJ
burst_energy = 0 # mJ
refresh_energy = 0 # mJ
power = 0 # mW
background_power = 0 # mW
actpre_power = 0 #mW
burst_power = 0 # mW
refresh_power = 0 # mW

fin = open("dramsim.dat", 'r')
fout = open('power.dat', 'w')

for line in fin:
    p = pattern.match(line)
        
    if p is not None:
        energy += float(p.group(13))
        background_energy += float(p.group(15))
        actpre_energy += float(p.group(17))
        burst_energy += float(p.group(19))
        refresh_energy += float(p.group(21))
        
        total_cycle = int(p.group(1))
                
    power = energy / (total_cycle * CYCLE_TIME)
    background_power = background_energy / (total_cycle * CYCLE_TIME)
    actpre_power = actpre_energy / (total_cycle * CYCLE_TIME)
    burst_power = burst_energy / (total_cycle * CYCLE_TIME)
    refresh_power = refresh_energy / (total_cycle * CYCLE_TIME)

print >>fout, "%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f" %(energy, power, background_energy, actpre_energy, burst_energy, refresh_energy, background_power, actpre_power, burst_power, refresh_power) 

fin.close()
fout.close()
