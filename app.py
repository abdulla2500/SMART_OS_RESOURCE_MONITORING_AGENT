import time
import pandas as pd
import streamlit as st

from resource_collector import get_system_resources
from process_monitor import get_top_processes
from decision_engine import analyze_system
from logger import save_log, read_logs

st.set_page_config(
    page_title="SMART OS RESOURCE MONITORING AGENT",
    layout="wide"
)

st.title("SMART OS RESOURCE MONITORING AGENT")

st.write(
    "A Python-based Operating Systems project that monitors CPU, RAM, disk, "
    "and running processes, then analyzes system health and recommends actions."
)

st.sidebar.header("Control Panel")

simulation_mode = st.sidebar.checkbox(
    "Use Simulation Mode",
    value=False
)

if simulation_mode:

    cpu_value = st.sidebar.slider(
        "Simulated CPU Usage (%)",
        0,
        100,
        90
    )

    ram_value = st.sidebar.slider(
        "Simulated RAM Usage (%)",
        0,
        100,
        88
    )

    disk_value = st.sidebar.slider(
        "Simulated Disk Usage (%)",
        0,
        100,
        70
    )

    resources = {
        "cpu_usage": cpu_value,
        "ram_usage": ram_value,
        "ram_used_gb": 0,
        "ram_total_gb": 0,
        "disk_usage": disk_value,
        "disk_used_gb": 0,
        "disk_total_gb": 0,
        "disk_free_gb": 0
    }

else:
    resources = get_system_resources()

top_processes = get_top_processes(limit=8)

analysis = analyze_system(
    resources,
    top_processes
)

save_log(
    resources,
    analysis
)

st.subheader("Live System Resource Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "CPU Usage",
        f"{resources['cpu_usage']}%"
    )
    st.progress(int(resources["cpu_usage"]))

with col2:
    st.metric(
        "RAM Usage",
        f"{resources['ram_usage']}%"
    )
    st.progress(int(resources["ram_usage"]))

with col3:
    st.metric(
        "Disk Usage",
        f"{resources['disk_usage']}%"
    )
    st.progress(int(resources["disk_usage"]))

st.subheader("Agent Decision")

if analysis["status"] == "Critical":
    st.error(
        f"System Status: {analysis['status']}"
    )

elif analysis["status"] == "Warning":
    st.warning(
        f"System Status: {analysis['status']}"
    )

else:
    st.success(
        f"System Status: {analysis['status']}"
    )

left_col, right_col = st.columns(2)

with left_col:

    st.subheader("Detected Problems")

    for problem in analysis["problems"]:
        st.write(f"- {problem}")

with right_col:

    st.subheader("Recommended Actions")

    for recommendation in analysis["recommendations"]:
        st.write(f"- {recommendation}")

st.subheader("Top Resource-Consuming Processes")

process_df = pd.DataFrame(top_processes)

if not process_df.empty:
    st.dataframe(
        process_df,
        use_container_width=True
    )

st.subheader("Resource Usage History")

logs = read_logs()

if not logs.empty:

    recent_logs = logs.tail(30)

    chart_data = recent_logs[
        ["cpu", "ram", "disk"]
    ]

    chart_data.index = recent_logs["time"]

    st.line_chart(chart_data)

st.subheader("Agentic AI Workflow")

st.write(
    """
    1. Observe → Collect CPU, RAM, Disk and Process data

    2. Analyze → Compare values with threshold rules

    3. Decide → Classify system as Normal, Warning or Critical

    4. Act → Recommend actions to improve performance
    """
)

st.sidebar.subheader("Auto Refresh")

auto_refresh = st.sidebar.checkbox(
    "Enable Auto Refresh",
    value=False
)

refresh_seconds = st.sidebar.slider(
    "Refresh Every Seconds",
    3,
    30,
    5
)

if auto_refresh:
    time.sleep(refresh_seconds)
    st.rerun()