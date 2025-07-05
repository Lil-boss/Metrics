import psutil
import asyncio
from prometheus_client import Gauge
from app import config

cpu_usage = Gauge("system_cpu_usage_percent", "System CPU usage percentage")
memory_usage = Gauge("system_memory_usage_percent", "System Memory usage percentage")
process_memory_usage = Gauge("process_memory_usage_percent", "Process Memory usage percentage")
process_start_time = Gauge("fastapi_process_start_time_seconds", "Process start time (seconds since epoch)")
process_uptime = Gauge("process_uptime_seconds", "Process uptime in seconds")
open_file_descriptors = Gauge("open_file_descriptors", "Number of open file descriptors")
garbage_collections = Gauge("gc_collections_total", "Number of garbage collections by generation", ["generation"])
thread_count = Gauge("python_thread_count", "Number of active threads")

async def collect_system_metrics():
    while True:
        cpu_usage.set(psutil.cpu_percent())
        memory_usage.set(psutil.virtual_memory().percent)
        process_memory_usage.set(psutil.Process().memory_percent())
        process_start_time.set(psutil.Process().create_time())
        process_uptime.set(psutil.Process().create_time() - psutil.boot_time())
        open_file_descriptors.set(psutil.Process().num_fds())
        garbage_collections.set(psutil.Process().num_fds())
        await asyncio.sleep(config.METRIC_UPDATE_INTERVAL)

def start_system_metrics_collection():
    loop = asyncio.get_event_loop()
    loop.create_task(collect_system_metrics())

