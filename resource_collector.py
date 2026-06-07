import os
import psutil


def convert_bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)


def get_system_resources():
    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()
    ram_usage = memory.percent

    disk = psutil.disk_usage(os.path.abspath(os.sep))
    disk_usage = disk.percent

    return {
        "cpu_usage": round(cpu_usage, 1),
        "ram_usage": round(ram_usage, 1),
        "ram_used_gb": convert_bytes_to_gb(memory.used),
        "ram_total_gb": convert_bytes_to_gb(memory.total),
        "disk_usage": round(disk_usage, 1),
        "disk_used_gb": convert_bytes_to_gb(disk.used),
        "disk_total_gb": convert_bytes_to_gb(disk.total),
        "disk_free_gb": convert_bytes_to_gb(disk.free)
    }


if __name__ == "__main__":
    print(get_system_resources())