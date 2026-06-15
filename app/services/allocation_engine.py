#from app.config import ALLOCATIONS
from app.config import settings

def allocate(amount: float):
    return {
        bucket: round(amount * ratio, 2)
        for bucket, ratio in settings.ALLOCATIONS.items()
    }