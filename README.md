# Event-Driven Ledger Allocation Engine

![Tests](https://github.com/mwapevi/Event-Driven-Ledger-Allocation-Engine/.github/workflows/test.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)

Backend system that processes incoming payment events and automatically allocates funds across internal ledger accounts.

## Overview

This project is a backend system that simulates how a financial platform might process incoming payment events and distribute funds across multiple internal ledger accounts.

The application receives payment completion events through a webhook endpoint, validates and processes them, then automatically allocates the incoming funds according to predefined rules.

The focus of the project is on backend architecture and reliability patterns commonly used in payment and fintech systems, including:

* Webhook processing
* Idempotent event handling
* Service-oriented design
* Automated fund allocation
* Audit logging
* Reconciliation tracking
* External API integration patterns

This project is intended as a portfolio and learning exercise and does not connect to any real banking infrastructure.

---

## Why I Built This

Many payment systems receive funds into a central account before distributing them internally for settlement, accounting, or operational purposes.

I built this to understand how systems handle payment-like workflows where:

- events can be retried
- delivery is not guaranteed exactly once
- processing must remain consistent even when duplicates occur

---

## System Flow

1. A payment completion event is received through a webhook.
2. The webhook signature is validated.
3. The event is checked against the idempotency store.
4. Previously processed events are ignored.
5. The allocation engine calculates ledger distributions.
6. Internal transfer requests are generated.
7. Transfer results are stored for auditing and reconciliation.
8. The event is marked as processed.

### Processing Pipeline

```text
External Payment Provider
           │
           ▼
Webhook Endpoint
           │
           ▼
Signature Verification
           │
           ▼
Idempotency Check
           │
           ▼
Event Processor
           │
           ▼
Allocation Engine
           │
           ▼
Transfer Client
           │
           ▼
Ledger Accounts
           │
           ▼
Audit & Reconciliation Store
```

---

## Project Structure

```text
.
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── db/
│   │   ├── session.py
│   │   └── base.py
│   │
│   ├── models/
│   │   ├── event.py
│   │   └── transfer.py
│   │
│   ├── schemas/
│   │   └── webhook.py
│   │
│   ├── routes/
│   │   └── webhook.py
│   │
│   ├── services/
│   │   ├── allocation_engine.py
│   │   ├── event_processor.py
│   │   ├── idempotency.py
│   │   ├── reconciliation.py
│   │   └── transfer_client.py
│   │
│   └── utils/
│       ├── logging.py
│       └── security.py
│
├── tests/
│   ├── test_allocation.py
│   ├── test_webhook.py
│   └── test_idempotency.py
│
└── docs/
    ├── architecture.md
    └── api_examples.md
```

---

## Tech Stack

* Python 3.12
* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker
* Pytest
* HTTP client (Requests / httpx)
  
## Key Components

### Webhook Processing

The application exposes an endpoint for receiving payment events from an external provider. Incoming requests are validated before any business logic is executed.

### Idempotency Layer

Idempotency is enforced using the event_id. In this implementation, processed events are tracked in the database to ensure duplicate webhook deliveries do not trigger multiple allocations.

### Allocation Engine

The allocation engine is responsible for calculating how incoming funds should be distributed across internal ledger accounts.

The default implementation performs an equal split across five accounts.

### Transfer Client

Transfers are executed through a dedicated client layer that abstracts communication with external services.

This keeps provider-specific logic separate from business rules and makes future integrations easier to support.

### Audit & Reconciliation

All processed events and transfer outcomes are recorded to provide traceability and support reconciliation workflows.

---

## Example Event Payload

```json
{
  "event_type": "deposit",
  "event_id": "evt_177",
  "amount": 500000,
  "account_id": "clearing_123",
  "timestamp": "2026-06-12T10:00:00Z"
}

```

---

## Allocation Example

Incoming Amount:

```text
500,000 ZMW
```

Default Allocation Rule:

```text
Account A → 100,000
Account B → 100,000
Account C → 100,000
Account D → 100,000
Account E → 100,000
```

If a remainder exists during division, it is assigned to the first account.

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

### Webhook Receiver

```http
POST /webhook/events
```

Receives incoming payment completion events from the external provider.

---

## Running Locally

### Clone the Repository

```bash
git clone https://github.com/mwapevi/Event-Driven-Ledger-Allocation-Engine.git
cd Event-Driven-Ledger-Allocation-Engine
```

### Configure Environment Variables

```bash
cp .env.example .env
```

Update the environment variables as needed.

### Start the Application

```bash
docker-compose up --build
```

### Access the Service

```text
API:  http://localhost:8000
Docs: http://localhost:8000/docs
```

---

## Running Tests

```bash
pytest
```

Current test coverage focuses on:

* Allocation calculations
* Webhook processing
* Idempotency behavior
* Service-level business logic

---

## Design Decisions

### Why Idempotency?

Webhook providers may deliver the same event multiple times.

Without idempotency protection, duplicate events could result in duplicate ledger allocations and inconsistent system state.

### Why Separate Services?

Business logic is intentionally kept outside route handlers to improve maintainability and make individual components easier to test.

### Why an Allocation Engine?

The allocation logic is isolated so that more sophisticated rules can be introduced later without changing the event-processing workflow.

---

## Future Improvements

Potential enhancements include:

* Kafka-based event streaming
* Change Data Capture (CDC) with Debezium
* Redis distributed locking
* Dead-letter queue support
* Dynamic allocation rules
* Multi-tenant account configurations
* Prometheus metrics
* Grafana dashboards
* Kubernetes deployment
* Event sourcing patterns

---

## Disclaimer

This project is a portfolio demonstration of backend patterns commonly used in financial systems.

It does not process real funds, connect to banking networks, or interact with production payment providers.

---

## Author

**Victor Mwape**

Backend Engineer with a focus on API integrations, event-driven architectures, fintech infrastructure, distributed systems, scalable backend services, and data pipelines.

GitHub: https://github.com/mwapevi

