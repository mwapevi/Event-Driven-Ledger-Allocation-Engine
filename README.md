# Event-Driven Ledger Allocation Engine

## Overview

This project demonstrates a production-style event-driven backend system that processes incoming financial events and automatically distributes funds into multiple internal ledger accounts.

The system simulates a banking integration using a generic external payment provider API and focuses on webhook processing, idempotent event handling, and automated fund allocation logic.

It is designed as a **fintech-grade backend architecture exercise**, not tied to any real banking institution.

---

## Business Problem

Modern financial systems often receive incoming payments into a central clearing ledger. These funds must be automatically distributed into multiple internal accounts based on predefined allocation rules.

This system solves:

* Automated processing of incoming deposit events
* Reliable distribution of funds across multiple accounts
* Prevention of duplicate processing
* Auditability and reconciliation of transactions

---

## System Architecture

External Payment Provider
↓
Webhook Event Delivery
↓
FastAPI Event Listener
↓
Signature Verification Layer
↓
Idempotency Control Layer
↓
Allocation Engine
↓
External Transfer API Adapter
↓
Internal Ledger Accounts
↓
Audit + Reconciliation Store

---

## Key Features

### 1. Event-Driven Processing

Receives incoming payment completion events via webhooks and triggers automated processing workflows.

### 2. Deterministic Allocation Engine

Splits incoming funds into multiple ledger accounts based on configurable rules.

### 3. Idempotent Event Handling

Ensures the same event cannot be processed multiple times, even under webhook retries.

### 4. External API Integration Layer

Abstracted payment provider client for initiating internal ledger transfers.

### 5. Retry & Failure Resilience

Implements exponential backoff retry for transient API failures.

### 6. Reconciliation Support

Tracks transfer status for downstream verification and auditability.

### 7. Audit Logging

Stores all processed events and resulting transfers for traceability.

---

## Tech Stack

* Python 3.12
* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker
* Pytest
* HTTP client (Requests / httpx)

---

## Core Workflow

1. External payment event is received via webhook
2. Event signature is validated
3. Event is checked against idempotency store
4. Incoming amount is parsed
5. Allocation engine splits funds into 5 internal accounts
6. Transfer API is called for each allocation
7. Results are stored in audit database
8. Event is marked as processed

---

## API Endpoints

### Health Check

```
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Webhook Receiver

```
POST /webhook/events
```

Receives incoming payment completion events from external provider.

---

## Example Event Payload (Generic)

```json
{
  "event_id": "evt_123456",
  "event_type": "payment.completed",
  "timestamp": "2026-06-01T10:30:00Z",
  "data": {
    "transaction_id": "txn_987654",
    "account_id": "clearing_account",
    "amount": 500000,
    "currency": "USD",
    "status": "completed"
  }
}
```

---

## Allocation Logic

Incoming Amount: 500,000 (cents)

Default Rule: Split equally across 5 accounts

* Account A: 100,000
* Account B: 100,000
* Account C: 100,000
* Account D: 100,000
* Account E: 100,000

Remainder handling is assigned to the first account.

---

## Project Structure

```
app/
├── main.py
├── config.py
├── routes/
│   └── webhook.py
├── services/
│   ├── allocation_engine.py
│   ├── event_processor.py
│   ├── transfer_client.py
│   ├── reconciliation.py
│   └── idempotency.py
├── models/
│   ├── event.py
│   └── transfer.py
├── db/
│   └── session.py
└── utils/
    ├── logging.py
    └── security.py
```

---

## Running Locally

### 1. Clone Repository

```bash
git clone https://github.com/mwapevi/Event-Driven-Ledger-Allocation-Engine
cd ledger-allocation-engine
```

### 2. Setup Environment

```bash
cp .env.example .env
```

### 3. Start with Docker

```bash
docker-compose up --build
```

### 4. Access Service

* API: http://localhost:8000
* Docs: http://localhost:8000/docs

---

## Testing

Run unit tests:

```bash
pytest
```

Covers:

* Allocation correctness
* Idempotency behavior
* Webhook processing
* Transfer client mocking

---

## Design Principles

* Event-driven architecture
* Stateless API layer
* Strong idempotency guarantees
* External system abstraction
* Fail-safe financial processing patterns
* Audit-first design

---

## Future Improvements

* Kafka-based event streaming
* Redis distributed locking
* Kubernetes deployment
* Prometheus + Grafana monitoring
* Dead-letter queue (DLQ)
* Multi-tenant allocation engine
* Dynamic rule engine for allocations

---

## Disclaimer

This project is a **portfolio demonstration system** simulating financial event processing.
It does not connect to real banking systems and does not process real funds.

---

## Author

Backend Engineer specializing in:

* API integrations
* Event-driven systems
* CVM Technology implementations
* Data pipelines
* Fintech infrastructure
