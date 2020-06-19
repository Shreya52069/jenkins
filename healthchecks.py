import shutil
import psutil

def check_usage_disk(disk) :
        du = shutil.disk_usage(disk)
        free = du.free/du.total*100
        return free > 20

def check_cpu_usage(second) :
        ku = psutil.cpu_percent(second)
        return ku < 75

if not check_usage_disk("/") or not check_cpu_usage():
        print("ERROR")
else :
        print("everything is okay")

