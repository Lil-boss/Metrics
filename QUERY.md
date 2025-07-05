# Prometheus Metric Queries: Purpose and Examples

This document explains **why** each Prometheus query is useful and **what** it returns, especially in the context of the FastAPI monitoring project.

---

## 🔄 1. Global Request Rate
```promql
rate(http_requests_total[5m])
```
Shows total request rate over time.

---

## 📊 2. Per-endpoint Request Rate
```promql
rate(http_requests_total{endpoint="/data"}[5m])
```
Track specific endpoint load.

---

## ⏱ 3. 95th Percentile Request Latency
```promql
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, endpoint))
```
Measure near-worst-case latency.

---

## 🕒 4. Process Uptime
```promql
time() - process_start_time_seconds{job="fastapi"}
```
Calculates uptime of the FastAPI process.

---

## 📈 5. Total Requests
```promql
sum(increase(http_requests_total{job="fastapi"}[$__range]))
```
Total number of requests during a time range.

---

## ❌ 6. Error Rate
```promql
(
  sum((increase(http_requests_total{job="fastapi",status_code=~"500"}[$__range]) or vector(0))) +
  sum((increase(http_requests_total{job="fastapi",status_code=~"500"}[$__range]) or vector(0)))
) / sum((increase(http_requests_total{job="fastapi"}[$__range])))
```
Calculates the proportion of 500 errors to total requests.

---

## ⌛ 7. Average Request Duration
```promql
sum(rate(http_request_duration_seconds_sum[$__range]) or vector(0)) / sum(rate(http_request_duration_seconds_count[$__range]) or vector(0))
```
Shows average duration per request.

---

## 🔄 8. Requests in Progress
```promql
sum(http_requests_progress_total{job="fastapi",endpoint!="/metrics"})
```
Currently active requests being processed.

---

## 🚀 9. API Throughput
```promql
rate(http_requests_total{job="fastapi"}[$__range])
```
Shows request per second rate.

---

## 📟 10. Requests by Status Code
```promql
sum(rate(http_requests_total{job="fastapi"}[5m])) by (status_code)
```
Shows request breakdown per HTTP status.

---

## 📉 11. API Latency (P50)
```promql
histogram_quantile(0.5, sum(rate(http_request_duration_seconds_bucket{job="fastapi"}[5m])) by (le))
```
Shows median (50th percentile) response time.

---

## ⌚ 12. Average Duration of Request
```promql
(rate(http_request_duration_seconds_sum[$__range])) / (rate(http_request_duration_seconds_count[$__range]))
```
Average response time for all requests.

---

## 🧠 13. CPU Usage
```promql
system_cpu_usage_percent{job="fastapi"}
```
Monitors CPU consumption.

---

## 🧮 14. Memory Usage
```promql
process_resident_memory_bytes{job="fastapi"}
process_virtual_memory_bytes{job="fastapi"}
process_memory_usage_percent{job="fastapi"}
```
Track memory usage stats: physical, virtual, and percentage.

---

## ♻️ 15. GC Collection Rate
```promql
rate(python_gc_collections_total{job="fastapi"}[$__range])
```
Observe how frequently Python's garbage collector runs.

---

## 📂 16. Open File Descriptors Ratio
```promql
process_open_fds{job="fastapi"} / process_max_fds{job="fastapi"}
```
Monitors how close the app is to the open file limit.

---

These queries are essential for building a robust observability layer, giving insights into usage patterns, system health, and application performance.
