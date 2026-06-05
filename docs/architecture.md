Include your Mermaid diagram:

```mermaid
flowchart TD

A[External Payment Provider]
--> B[Webhook Receiver]

B --> C[Signature Validation]

C --> D[Idempotency Check]

D --> E[Allocation Engine]

E --> F[Ledger Account A]
E --> G[Ledger Account B]
E --> H[Ledger Account C]
E --> I[Ledger Account D]
E --> J[Ledger Account E]

E --> K[Transfer Adapter]

K --> L[External API]

L --> M[Reconciliation]

M --> N[Audit Store]
```
