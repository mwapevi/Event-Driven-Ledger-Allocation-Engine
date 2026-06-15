from app.config import settings

def allocate(amount: float) -> dict:
    return {
        account: round(amount * ratio, 2)
        for account, ratio in settings.ALLOCATIONS.items()
    }