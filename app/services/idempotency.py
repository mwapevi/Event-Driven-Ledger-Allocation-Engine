import os
import redis
import logging

# -----------------------------
# Redis initialization (SAFE)
# -----------------------------
redis_client = None

REDIS_URL = os.getenv("REDIS_URL")

if REDIS_URL:
    try:
        redis_client = redis.Redis.from_url(REDIS_URL)
        redis_client.ping()
    except Exception as e:
        logging.warning(f"Redis disabled: {e}")
        redis_client = None
else:
    logging.warning("REDIS_URL not set; idempotency will use fallback memory mode")


# -----------------------------
# Fallback in-memory store
# -----------------------------
processed_events = set()


def is_duplicate(event_id: str) -> bool:
    # If Redis is available, use it
    if redis_client:
        return redis_client.exists(event_id) == 1

    # fallback
    return event_id in processed_events


def mark_processed(event_id: str):
    if redis_client:
        # store with no expiration (you can add TTL later)
        redis_client.set(event_id, "1")
    else:
        processed_events.add(event_id)