import time
import psutil


def get_top_processes(limit=8):
    process_objects = []
    process_list = []

    for process in psutil.process_iter(["pid", "name"]):
        try:
            if process.info["name"] == "System Idle Process":
                continue

            process.cpu_percent(interval=None)
            process_objects.append(process)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    time.sleep(0.3)

    for process in process_objects:
        try:
            cpu_usage = process.cpu_percent(interval=None)
            memory_usage_mb = process.memory_info().rss / (1024 ** 2)

            process_list.append({
                "PID": process.pid,
                "Process Name": process.name(),
                "CPU %": round(cpu_usage, 1),
                "RAM MB": round(memory_usage_mb, 1)
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    process_list = sorted(
        process_list,
        key=lambda item: (item["CPU %"], item["RAM MB"]),
        reverse=True
    )

    return process_list[:limit]


if __name__ == "__main__":
    for process in get_top_processes():
        print(process)