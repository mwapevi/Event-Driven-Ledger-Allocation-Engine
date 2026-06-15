import uuid
import logging
import time


class TransferClient:

    def create_book_transfer(self, source, destination, amount, retries=3):
        for attempt in range(retries):
            try:
                transfer_id = str(uuid.uuid4())
               

                logging.info(
                    f"[TRANSFER attempt={attempt+1}] {source} → {destination} | {amount}"
                )

                return {
                    "transfer_id": transfer_id,
                    "status": "success"
                }

            except Exception as e:
                logging.error(f"Transfer failed: {e}")

                if attempt == retries - 1:
                    raise

                time.sleep(2 ** attempt)