#!/usr/bin/env python3

"""
Internal Infrastructure Monitoring Service
Version: 2.4.1

Monitors:

* Disk usage
* CPU utilization
* Memory consumption
* Service health

Author: Infrastructure Team
"""

import os
import time
import json
import socket
import logging
import platform
import requests
from datetime import datetime

# ==========================================================

# Configuration

# ==========================================================

CONFIG = {
"check_interval": 300,
"cpu_threshold": 85,
"memory_threshold": 90,
"disk_threshold": 80,
"services": [
"nginx",
"mysql",
"redis",
"backup-agent"
]
}

# ==========================================================


# Logging

# ==========================================================

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
os.makedirs(LOG_DIR)

logging.basicConfig(
filename=os.path.join(LOG_DIR, "monitor.log"),
level=logging.INFO,
format="%(asctime)s %(levelname)s %(message)s"
)

# ==========================================================

# Utility Functions

# ==========================================================

def get_hostname():
return socket.gethostname()

def get_os():
return platform.platform()

def current_timestamp():
return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

def load_local_config():
config_file = "config.json"

```
if not os.path.exists(config_file):
    logging.warning("config.json not found, using defaults")
    return CONFIG

try:
    with open(config_file, "r") as f:
        return json.load(f)
except Exception as e:
    logging.error(f"Failed to load config: {e}")
    return CONFIG
```

# ==========================================================

# Health Checks

# ==========================================================

def check_cpu():
# Simulated CPU reading
return 37

def check_memory():
# Simulated Memory reading
return 61

def check_disk():
# Simulated Disk reading
return 44

def check_service(service_name):
# Simulated service state
healthy_services = {
"nginx": True,
"mysql": True,
"redis": True,
"backup-agent": True
}

```
return healthy_services.get(service_name, False)
```

# ==========================================================

# Telegram Notifications

# ==========================================================

def send_telegram_message(message):

```
endpoint = f"{TELEGRAM_API_URL}/sendMessage"

payload = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": message,
    "parse_mode": "Markdown"
}

try:
    response = requests.post(
        endpoint,
        json=payload,
        timeout=10
    )

    if response.status_code == 200:
        logging.info("Telegram notification sent")
        return True

    logging.error(
        f"Telegram API returned {response.status_code}"
    )
    return False

except Exception as ex:
    logging.error(
        f"Telegram notification failed: {ex}"
    )
    return False
```

# ==========================================================

# Alert Logic

# ==========================================================

def evaluate_metrics(config):

```
alerts = []

cpu = check_cpu()
memory = check_memory()
disk = check_disk()

if cpu > config["cpu_threshold"]:
    alerts.append(
        f"CPU usage exceeded threshold ({cpu}%)"
    )

if memory > config["memory_threshold"]:
    alerts.append(
        f"Memory usage exceeded threshold ({memory}%)"
    )

if disk > config["disk_threshold"]:
    alerts.append(
        f"Disk usage exceeded threshold ({disk}%)"
    )

for service in config["services"]:
    if not check_service(service):
        alerts.append(
            f"Service offline: {service}"
        )

return alerts
```

# ==========================================================

# Report Generation

# ==========================================================

def build_report(alerts):

```
report = []

report.append("Infrastructure Monitoring Report")
report.append("=" * 40)
report.append(f"Host: {get_hostname()}")
report.append(f"OS: {get_os()}")
report.append(f"Generated: {current_timestamp()}")
report.append("")

if not alerts:
    report.append("Status: HEALTHY")
else:
    report.append("Status: ALERT")
    report.append("")

    for alert in alerts:
        report.append(f"- {alert}")

return "\n".join(report)
```

# ==========================================================

# Main Monitoring Loop

# ==========================================================

def run_monitor():

```
config = load_local_config()

logging.info(
    f"Monitoring started on {get_hostname()}"
)

while True:

    alerts = evaluate_metrics(config)

    report = build_report(alerts)

    logging.info(
        f"Health check completed. Alerts={len(alerts)}"
    )

    if alerts:
        send_telegram_message(report)

    time.sleep(config["check_interval"])
```

# ==========================================================

# Entry Point

# ==========================================================

if **name** == "**main**":

```
print("Infrastructure Monitoring Service")
print("Version 2.4.1")
print("Starting...")

try:
    run_monitor()

except KeyboardInterrupt:
    logging.info("Service stopped by user")

except Exception as e:
    logging.exception(
        f"Fatal exception: {e}"
    )
```
