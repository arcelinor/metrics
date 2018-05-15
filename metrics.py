#!/usr/bin/python
import argparse, psutil
parser = argparse.ArgumentParser()
parser.add_argument("parameter", help = "Use \"cpu\" to show CPU usage metrics. Use \"mem\" to show memory usage metrics")
args = parser.parse_args()
if args.parameter == "cpu":
    cpumetrics = psutil.cpu_times_percent(interval = 1)
    print ("system.cpu.idle " + str(cpumetrics[3]))
    print ("system.cpu.user " + str(cpumetrics[0]))
    print ("system.cpu.guest " + str(cpumetrics[8]))
    print ("system.cpu.iowait " + str(cpumetrics[4]))
    print ("system.cpu.stolen " + str(cpumetrics[7]))
    print ("system.cpu.system " + str(cpumetrics[2]))
elif args.parameter == "mem":
    virtualmem = psutil.virtual_memory()
    swapmem = psutil.swap_memory()
    print ("virtual total " + str(virtualmem[0]))
    print ("virtual used " + str(virtualmem[3]))
    print ("virtual free " + str(virtualmem[4]))
    print ("virtual shared " + str(virtualmem[9]))
    print ("swap total " + str(swapmem[0]))
    print ("swap used " + str(swapmem[1]))
    print ("swap free " + str(swapmem[2]))
else:
    print ("Incorrect parameter, use -h or --help for available options")
