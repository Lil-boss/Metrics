import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "http_requests_total", "Total HTTP requests", ["method", "endpoint", "status_code"]
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency",
    ["method", "endpoint"],
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10),
)

REQUEST_PROGRESS = Counter(
    "http_requests_progress", "Progress of HTTP requests", ["method", "endpoint"]
)

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        method = request.method
        endpoint = request.url.path
        status_code = str(response.status_code)

        REQUEST_COUNT.labels(method, endpoint, status_code).inc()
        REQUEST_LATENCY.labels(method, endpoint).observe(process_time)
        REQUEST_PROGRESS.labels(method, endpoint).inc()

        return response
