from app.models.transfer import TransferAudit

def get_event_transfers(
        db,
        event_id):

    return db.query(
        TransferAudit
    ).filter(
        TransferAudit.event_id
        == event_id
    ).all()
