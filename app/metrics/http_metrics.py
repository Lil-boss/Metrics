from prometheus_client import Counter, Histogram
from app import config

http_requests_total = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status_code"]
)

http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "Histogram of request duration",
    ["method", "endpoint"],
    buckets=config.HISTOGRAM_BUCKETS
)
