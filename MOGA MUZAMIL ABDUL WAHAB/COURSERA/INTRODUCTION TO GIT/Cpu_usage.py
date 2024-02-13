import psutil

def check_cpu_usage(percent):

    usage = psutil.cpu_percent()

    return usage < percent
