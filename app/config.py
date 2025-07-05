# Interval in seconds for updating system metrics (CPU, memory)
METRIC_UPDATE_INTERVAL = 2

# Custom histogram buckets (used in metrics middleware & http_metrics)
HISTOGRAM_BUCKETS = (
    0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0
)
