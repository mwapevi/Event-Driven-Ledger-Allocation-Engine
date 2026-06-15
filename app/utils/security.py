import hmac
import hashlib

def verify_signature(
        payload: bytes,
        signature: str,
        secret: str):

    digest = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(
        digest,
        signature
    )