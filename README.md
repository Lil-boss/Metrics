# FastAPI Metrics Monitoring App

This project is a FastAPI-based web application with built-in Prometheus metrics collection and visualization support via Grafana.

## 🚀 Features
- FastAPI core with async endpoints
- `/metrics` Prometheus-compatible endpoint
- Middleware to log HTTP request metrics
- Background system metrics collection: CPU, memory, uptime, threads, GC, file descriptors
- Docker Compose setup with Prometheus and Grafana

## 📦 Endpoints
| Method | Path      | Description               |
|--------|-----------|---------------------------|
| GET    | `/`       | Root welcome endpoint     |
| GET    | `/health` | Health check              |
| GET    | `/metrics`| Prometheus metrics scrape |
| POST   | `/data`   | Accepts JSON payload      |
| GET    | `/data`   | Returns stored payloads   |

## 📊 Observability Stack
- **Prometheus** for metric scraping
- **Grafana** for dashboards

## 🐳 Docker Compose Usage
```bash
  docker-compose up --build
```

### Access Services:
- FastAPI: [http://localhost:8000](http://localhost:8000)
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3000](http://localhost:3000)

## 📈 Grafana Setup
1. Log into Grafana (default: admin / admin)
2. Add **Prometheus** data source: `http://prometheus:9090`
3. Import dashboards or create custom panels

## 📁 Project Structure
```
fastapi-metrics-app/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── middleware/metrics_middleware.py
│   ├── metrics/
│   │   ├── http_metrics.py
│   │   ├── system_metrics.py
│   ├── routers/
│   │   ├── api.py
│   │   ├── health.py
├── prometheus.yml
├── docker-compose.yml
├── Dockerfile
├── README.md
```

## ✅ Requirements
- Python 3.8+
- Docker + Docker Compose

## 📃 License
MIT

- [Query Reference Guide](./QUERY.md)
