import logging

logging.basicConfig(
    filename="Allocation.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(
    "profitflow"
)
logging.info({
    "event": "transfer_created",
    "source": source,
    "destination": destination,
    "amount": amount
})
