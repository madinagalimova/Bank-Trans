# Bank-Trans: Real-Time Transaction Processing System

> A minimal prototype for ingesting and validating financial transactions via Kafka (Redpanda).

---

## 🚀 Overview

This project consists of two core services:

- **Transaction Generator**: Simulates bank transactions and publishes them to a Kafka topic.
- **Stream Processor**: Consumes these transactions, validates them using `pydantic`, and prepares for further processing (e.g. rule engine, alerts, DB).

> Built for local experimentation using [Redpanda](https://redpanda.com/) as the Kafka engine.





## 🧪 Requirements

Python 3.10+  
Kafka broker (tested with Redpanda)  
Virtualenv or Poetry recommended

Install dependencies:

```bash
pip install -r requirements.txt
````

---

## ⚙️ Running the System

### 1. Start Redpanda cluster (example with Docker)

```bash
rpk container start -n 3
```

### 2. Start the Transaction Generator

```bash
python src/test_tx_generator.py
```

### 3. Start the Stream Processor

```bash
python src/stream_proc.py
```

---

## 📦 Dependencies

Key packages (see `pip list`):

* `aiokafka`, `kafka-python` – Kafka producers & consumers
* `pydantic v2` – Runtime validation
* `faust`, `croniter` – Future stream & rule-based extensions

---

## 🗺️ Roadmap

* [ ] Rule engine for fraud/anomaly detection
* [ ] Persistence layer (PostgreSQL / ClickHouse / SQLite)
* [ ] Alerting mechanism (email, Telegram, etc.)
* [ ] Dashboard & REST API (FastAPI + Grafana/Streamlit)

---

## 🛡️ License

MIT

---

## 🤝 Contribution

This project is in early development. Contributions, feedback, and testing are welcome.

---
