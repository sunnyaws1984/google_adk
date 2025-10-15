"""
Simple CPU Information Tool
"""

import time
import psutil


def get_cpu_info():
    """
    Returns basic CPU information including core count and average usage.
    """
    try:
        physical_cores = psutil.cpu_count(logical=False)
        avg_usage = psutil.cpu_percent(interval=1)

        return {
            "physical_cores": physical_cores,
            "avg_cpu_usage": f"{avg_usage:.1f}%",
            "high_usage": avg_usage > 80,
            "timestamp": time.time(),
        }

    except Exception as e:
        return {
            "error": f"Failed to get CPU info: {e}",
            "timestamp": time.time(),
        }
