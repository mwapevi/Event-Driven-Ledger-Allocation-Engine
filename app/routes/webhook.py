from fastapi import APIRouter

router = APIRouter()


@router.post("/webhook/events")
async def receive_event(
    payload: dict
):

    return {
        "message": "event received",
        "event_id": payload["event_id"]
    }
