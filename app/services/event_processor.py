from app.services.allocation_engine import allocate
from app.services.transfer_client import TransferClient
from app.services.idempotency import is_duplicate, mark_processed
from app.models.event import Event
from app.models.transfer import Transfer
from app.models.allocation import Allocation   # <-- NEW
from datetime import datetime, UTC
from datetime import datetime

created_at = datetime.now(UTC)
from datetime import datetime

BUCKET_MAP = {
    "ACCOUNT A": "ACCOUNT A",
    "ACCOUNT B": "ACCOUNT B",
    "ACCOUNT C": "ACCOUNT C",
    "ACCOUNT D": "ACCOUNT D",
    "ACCOUNT E": "ACCOUNT E",
}


def process_event(db, event):
    # 1. Idempotency check
    if is_duplicate(event.event_id):
        return {"status": "ignored_duplicate", "event_id": event.event_id}

    mark_processed(event.event_id)

    # 2. Allocation
    allocations = allocate(event.amount)

    # 3. Save event
    db_event = Event(
        id=event.event_id,
        event_type=event.event_type,
        raw_payload=str(event),
        created_at=datetime.utcnow()
    )
    db.add(db_event)

    client = TransferClient()
    transfers = []

    # 4. Create transfers + persist them
    for account, amount in allocations.items():
        if amount <= 0:
            continue

        result = client.create_book_transfer(
            source="clearing_account",
            destination=BUCKET_MAP[account],
            amount=amount
        )

        # Existing transfer record
        db_transfer = Transfer(
            event_id=event.event_id,
            amount=amount,
            created_at=datetime.utcnow()
        )
        db.add(db_transfer)

        # NEW: Allocation record
        db_allocation = Allocation(
            event_id=event.event_id,
            account=account,
            amount=amount,
            transfer_id=result.get("transfer_id"),
            status=result.get("status"),
            created_at=datetime.utcnow()
        )
        db.add(db_allocation)

        transfers.append({
            "account": account,
            "amount": amount,
            "transfer": result
        })

    # 5. COMMIT EVERYTHING
    db.commit()

    return {
        "event_id": event.event_id,
        "allocations": allocations,
        "transfers": transfers
    }