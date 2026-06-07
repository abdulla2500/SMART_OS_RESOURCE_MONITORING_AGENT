# SMART OS RESOURCE MONITORING AGENT

## Project Overview

SMART OS RESOURCE MONITORING AGENT is a Python-based Operating Systems project that monitors CPU usage, RAM usage, disk usage, and running processes in real time.

The system analyzes the current resource usage and classifies the computer condition as Normal, Warning, or Critical. It also recommends actions to help improve system performance.

## Problem Solved

Many users experience slow computer performance but do not know the exact reason. The problem may come from high CPU usage, high memory usage, disk storage problems, or heavy background processes.

This project helps users identify the cause of system slowdown and gives useful recommendations.

## Main Features

- Real-time CPU monitoring
- Real-time RAM monitoring
- Disk usage monitoring
- Top resource-consuming process detection
- Agent-based decision making
- System status classification: Normal, Warning, Critical
- Recommended actions for the user
- CSV history logging
- Resource usage history graph
- Simulation mode for testing and presentation
- Streamlit dashboard interface

## Technologies Used

- Python
- psutil
- Streamlit
- Pandas
- CSV file logging

## Operating Systems Concepts Used

This project is related to Operating Systems because it demonstrates:

- Process management
- CPU usage monitoring
- Memory management
- Disk management
- Resource allocation
- System performance monitoring

## Agentic AI Workflow

The system follows an agentic workflow:

1. Observe: Collect CPU, RAM, disk, and process data.
2. Analyze: Compare the collected values with threshold rules.
3. Decide: Classify the system as Normal, Warning, or Critical.
4. Act: Recommend actions to improve performance.

## System Status Rules

CPU:
- Below 60% = Normal
- 60% to 85% = Warning
- Above 85% = Critical

RAM:
- Below 70% = Normal
- 70% to 85% = Warning
- Above 85% = Critical

Disk:
- Below 75% = Normal
- 75% to 90% = Warning
- Above 90% = Critical

## How to Run the Project

First activate the virtual environment:

```bash
venv\Scripts\activate'''text 