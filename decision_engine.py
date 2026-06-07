def analyze_system(resources, top_processes):
    cpu = resources["cpu_usage"]
    ram = resources["ram_usage"]
    disk = resources["disk_usage"]

    status = "Normal"
    problems = []
    recommendations = []

    def upgrade_status(new_status):
        nonlocal status
        if new_status == "Critical":
            status = "Critical"
        elif new_status == "Warning" and status != "Critical":
            status = "Warning"

    top_cpu_process = None
    top_ram_process = None

    if top_processes:
        top_cpu_process = max(top_processes, key=lambda x: x["CPU %"])
        top_ram_process = max(top_processes, key=lambda x: x["RAM MB"])

    if cpu > 85:
        upgrade_status("Critical")
        problems.append(f"CPU usage is critical at {cpu}%.")
        if top_cpu_process:
            recommendations.append(f"Check '{top_cpu_process['Process Name']}' because it is using high CPU.")
        recommendations.append("Close unnecessary applications to reduce CPU load.")
    elif cpu > 60:
        upgrade_status("Warning")
        problems.append(f"CPU usage is high at {cpu}%.")
        recommendations.append("Avoid running too many heavy programs at the same time.")

    if ram > 85:
        upgrade_status("Critical")
        problems.append(f"RAM usage is critical at {ram}%.")
        if top_ram_process:
            recommendations.append(f"Check '{top_ram_process['Process Name']}' because it is using high memory.")
        recommendations.append("Close unused browser tabs or memory-heavy applications.")
    elif ram > 70:
        upgrade_status("Warning")
        problems.append(f"RAM usage is high at {ram}%.")
        recommendations.append("Reduce multitasking to free memory.")

    if disk > 90:
        upgrade_status("Critical")
        problems.append(f"Disk usage is critical at {disk}%.")
        recommendations.append("Delete unnecessary files or move old files to external storage.")
    elif disk > 75:
        upgrade_status("Warning")
        problems.append(f"Disk usage is high at {disk}%.")
        recommendations.append("Clean old downloads, temporary files, or unused applications.")

    if not problems:
        problems.append("System resources are working normally.")
        recommendations.append("No immediate action is required.")

    return {
        "status": status,
        "problems": problems,
        "recommendations": recommendations
    }


if __name__ == "__main__":
    fake_resources = {
        "cpu_usage": 90,
        "ram_usage": 80,
        "disk_usage": 60
    }

    fake_processes = [
        {"PID": 1, "Process Name": "chrome.exe", "CPU %": 35, "RAM MB": 900}
    ]

    print(analyze_system(fake_resources, fake_processes))