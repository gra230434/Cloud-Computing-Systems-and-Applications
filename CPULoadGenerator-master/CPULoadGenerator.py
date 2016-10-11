#!/usr/bin/python


import multiprocessing
from twisted.python import usage
import sys
sys.path.insert(0, 'utils')

from Monitor import MonitorThread
from Controller import ControllerThread
from closedLoopActuator import closedLoopActuator


class Options(usage.Options):
    """
       Defines the default input parameters
    """
    optParameters = [
            ["cpuLoad", "l", 0.2, "Cpu Target Load", float],
            ["duration", "d", 10, "Duration", int],
            ["cpu_core", "c", 0, "Select the CPU on which generate the load",
                int]
        ]

if __name__ == "__main__":

    import sys
    options = Options()
    try:
        options.parseOptions()
    except Exception:
        print '%s: %s' % (sys.argv[0], e)
        print '%s: Try --help for usage details.' % (sys.argv[0])
        sys.exit(1)
    else:
        if options['cpuLoad'] < 0 or options['cpuLoad'] > 1:
            print "CPU target load out of the range [0,1]"
            sys.exit(1)
        if options['duration'] < 0:
            print "Invalid duration"
            sys.exit(1)
        if options['cpu_core'] > multiprocessing.cpu_count():
            print("You have only %d cores on your machine" % multiprocessing.cpu_count())
            sys.exit(1)

    if options['cpu_core'] = multiprocessing.cpu_count():
        print("You have only %d cores on your machine" % multiprocessing.cpu_count())
        if multiprocessing.cpu_count() = 4:
            monitor0 = MonitorThread(0, 0.1)
            monitor1 = MonitorThread(1, 0.1)
            monitor2 = MonitorThread(2, 0.1)
            monitor3 = MonitorThread(3, 0.1)
            monitor0.start()
            monitor1.start()
            monitor2.start()
            monitor3.start()
            control0 = ControllerThread(0.1)
            control0.start()
            control0.setCpuTarget(options['cpuLoad'])
            control1 = ControllerThread(0.1)
            control1.start()
            control1.setCpuTarget(options['cpuLoad'])
            control2 = ControllerThread(0.1)
            control2.start()
            control2.setCpuTarget(options['cpuLoad'])
            control3 = ControllerThread(0.1)
            control3.start()
            control3.setCpuTarget(options['cpuLoad'])
            actuator0 = closedLoopActuator(control0, monitor0, options['duration'], options['cpu_core'], options['cpuLoad'])
            actuator0.run()
            actuator1 = closedLoopActuator(control0, monitor0, options['duration'], options['cpu_core'], options['cpuLoad'])
            actuator1.run()
            actuator2 = closedLoopActuator(control0, monitor0, options['duration'], options['cpu_core'], options['cpuLoad'])
            actuator2.run()
            actuator3 = closedLoopActuator(control0, monitor0, options['duration'], options['cpu_core'], options['cpuLoad'])
            actuator3.run()
            monitor0.running = 0
            monitor1.running = 0
            monitor2.running = 0
            monitor3.running = 0
            control0.running = 0
            control1.running = 0
            control2.running = 0
            control3.running = 0
            monitor0.join()
            monitor1.join()
            monitor2.join()
            monitor3.join()
            control0.join()
            control1.join()
            control2.join()
            control3.join()
        else:
            print("we can't do anything")
    else:
        monitor = MonitorThread(options['cpu_core'], 0.1)
        monitor.start()

        control = ControllerThread(0.1)
        control.start()
        control.setCpuTarget(options['cpuLoad'])

        actuator = closedLoopActuator(control, monitor, options['duration'], options['cpu_core'], options['cpuLoad'])
        actuator.run()

        monitor.running = 0
        control.running = 0
        monitor.join()
        control.join()
