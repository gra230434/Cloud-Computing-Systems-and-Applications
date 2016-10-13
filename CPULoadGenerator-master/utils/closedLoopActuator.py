import time


class closedLoopActuator():
    """
        Generates CPU load by tuning the sleep time
    """
    def __init__(self, controller, monitor, duration, cpu_core, target):
        self.controller = controller
        self.monitor = monitor
        self.duration = duration
        self.target = target
        self.controller.setCpu(self.monitor.getCpuLoad())
        self.period = 0.05 # actuation period  in seconds
        self.start_time = time.time()

    def generate_load(self, sleep_time):
        interval = time.time() + self.period - sleep_time
        # generates some getCpuLoad for interval seconds
        while (time.time() < interval):
            pr = 213123  # generates some load
            pr * pr
            pr = pr + 1
        time.sleep(sleep_time)

    def run(self):
        while (time.time() - self.start_time) <= self.duration:
            self.controller.setCpu(self.monitor.getCpuLoad())
            sleep_time = self.controller.getSleepTime()
            self.generate_load(sleep_time)
        return sleep_time
