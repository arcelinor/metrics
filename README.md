
# metrics

Metrics python script is designed to display number of CPU and memory metrics on the system where it runs. 

## Getting Started

Python 2.6 to 3.6 interpreter is needed to run the script.
Metrics script displays a floats representing the current system-wide CPU and memory utilization as a percentage.
It shows following CPU metrics (for 1 second interval):

| Metric | Description |
| ------ | ------ |
| system.cpu.idle | time spent doing nothing |
| system.cpu.user | time spent by normal processes executing in user mode; on Linux this also includes guest time |
| system.cpu.guest |  (Linux 2.6.24+): time spent running a virtual CPU for guest operating systems under the control of the Linux kernel |
| system.cpu.iowait | (Linux): time spent waiting for I/O to complete |
| system.cpu.stolen | (Linux 2.6.11+): time spent by other operating systems running in a virtualized environment |
| system.cpu.system | time spent by processes executing in kernel mode |

And the following system memory metrics:

| Metric | Description |
| ------ | ------ |
| virtual total | total physical memory |
| virtual used | memory used, calculated differently depending on the platform and designed for informational purposes only. Total - free does not necessarily match used |
| virtual free | memory not being used at all (zeroed) that is readily available; note that this doesn’t reflect the actual memory available (use available instead). total - used does not necessarily match free |
| virtual shared | (Linux, BSD): memory that may be simultaneously accessed by multiple processes |
| swap total | total swap memory in bytes |
| swap used | used swap memory in byte |
| swap free | free swap memory in bytes |

## Prerequisites

To run Metrics script you need psutil, cross-platform library for retrieving information on running processes and system utilization. It can be installed with pip: 

```
pip install psutil
```

## Usage

Metrics script accepts one parameter from the followng list:

| Parameter | Function |
| ------ | ------ |
| -h or --help | Displays usage help |
| cpu | Displays CPU metrics |
| mem | Displays memory metrics |

### Example:

```
./metrics cpu
```

![alt text](https://raw.githubusercontent.com/arcelinor/metrics/master/Metrics_cpu.PNG)

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE.md](https://github.com/arcelinor/metrics/blob/master/LICENSE) file for details

