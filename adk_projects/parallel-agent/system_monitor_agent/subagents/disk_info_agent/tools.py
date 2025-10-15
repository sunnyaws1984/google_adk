"""
Simple Disk Information Tool
"""

import time
import psutil


def get_disk_info():
    """
    Returns basic disk information including partitions, usage, and alerts.
    """
    try:
        partitions = []
        total_space = 0
        used_space = 0
        high_usage_partitions = []

        for p in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(p.mountpoint)

                partitions.append({
                    "device": p.device,
                    "mountpoint": p.mountpoint,
                    "filesystem": p.fstype,
                    "total_gb": round(usage.total / (1024**3), 2),
                    "used_gb": round(usage.used / (1024**3), 2),
                    "free_gb": round(usage.free / (1024**3), 2),
                    "usage_percent": round(usage.percent, 1),
                })

                total_space += usage.total
                used_space += usage.used

                if usage.percent > 85:
                    high_usage_partitions.append(p.mountpoint)

            except (PermissionError, FileNotFoundError):
                # Skip inaccessible partitions
                continue

        overall_usage = (used_space / total_space * 100) if total_space else 0

        return {
            "partitions": partitions,
            "total_space_gb": round(total_space / (1024**3), 2),
            "used_space_gb": round(used_space / (1024**3), 2),
            "overall_usage_percent": round(overall_usage, 1),
            "high_usage_partitions": high_usage_partitions or None,
            "timestamp": time.time(),
        }

    except Exception as e:
        return {
            "error": f"Failed to get disk info: {e}",
            "timestamp": time.time(),
        }
