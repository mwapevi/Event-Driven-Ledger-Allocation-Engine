from app.services.allocation_engine import allocate

def test_allocate():
    result = allocate(100)

    assert sum(result.values()) == 100
    assert len(result) == 5


