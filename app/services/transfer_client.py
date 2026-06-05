import httpx


class TransferClient:

    def __init__(
        self,
        base_url: str
    ):
        self.base_url = base_url

    async def transfer(
        self,
        source_account,
        destination_account,
        amount
    ):

        return {
            "source": source_account,
            "destination": destination_account,
            "amount": amount,
            "status": "success"
        }
