import csv
import os
from datetime import datetime

import pandas as pd

LOG_FILE = "system_logs.csv"


def save_log(resources, analysis):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["time", "cpu", "ram", "disk", "status"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            resources["cpu_usage"],
            resources["ram_usage"],
            resources["disk_usage"],
            analysis["status"]
        ])


def read_logs():
    if not os.path.exists(LOG_FILE):
        return pd.DataFrame(
            columns=["time", "cpu", "ram", "disk", "status"]
        )

    return pd.read_csv(LOG_FILE)


if __name__ == "__main__":
    print("Logger module loaded successfully.")