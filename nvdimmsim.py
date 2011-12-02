#!/usr/bin/python -O

import sys
import re

EPOCH_COUNT = 100000
CYCLE_TIME = float(1) / 667000000

#workload = sys.argv[1]
#fout_name = sys.argv[2]

idle_energy_pattern = re.compile("Accumulated Idle Energy: ([0-9\.]+) mJ")
access_energy_pattern = re.compile("Accumulated Access Energy: ([0-9\.]+) mJ")
erase_energy_pattern = re.compile("Accumulated Erase Energy: ([0-9\.]+) mJ")
energy_pattern = re.compile("Total Energy: ([0-9\.]+) mJ")
idle_power_pattern = re.compile("Average Idle Power: ([0-9\.]+) mW")
access_power_pattern = re.compile("Average Access Power: ([0-9\.]+) mW")
erase_power_pattern = re.compile("Average Erase Power: ([0-9\.]+) mW")
power_pattern = re.compile("Average Power: ([0-9\.]+) mW")

idle_energy = 0
access_energy = 0
erase_energy = 0
energy = 0
idle_power = 0
access_power = 0
erase_power = 0
power = 0

fin = open('../nvdimm_logs/NVDIMM.log', 'r')
fout = open('nvdimmsim.dat', 'w')
    
for line in fin:
    ie = idle_energy_pattern.match(line)
    ae = access_energy_pattern.match(line)
    ee = erase_energy_pattern.match(line)
    e = energy_pattern.match(line)
    ip = idle_power_pattern.match(line)
    ap = access_power_pattern.match(line)
    ep = erase_power_pattern.match(line)
    p = power_pattern.match(line)

    if ie is not None: idle_energy += float(ie.group(1))
    elif ae is not None: access_energy += float(ae.group(1))
    elif ee is not None: erase_energy += float(ee.group(1))
    elif e is not None: energy += float(e.group(1))
    elif ip is not None: idle_power += float(ip.group(1))
    elif ap is not None: access_power += float(ap.group(1))
    elif ep is not None: erase_power += float(ep.group(1))
    elif p is not None: power += float(p.group(1))

print >>fout, "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %(energy, power, idle_energy, access_energy, erase_energy, idle_power, access_power, erase_power)

fin.close()
fout.close()
