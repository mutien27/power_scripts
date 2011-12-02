#!/bin/bash

./dramsim.py
./power.py
./nvdimmsim.py

cat power.dat nvdimmsim.dat

# OUTPUT:
# - power.dat: dram power (energy, power, background_energy, actpre_energy, burst_energy, refresh_energy, background_power, actpre_power, burst_power, refresh_power)
# - nvdimmsim.dat: nv power (energy, power, idle_energy, access_energy, erase_energy, idle_power, access_power, erase_power)