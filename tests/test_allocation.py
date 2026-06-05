from app.services.allocation_engine import allocate


def test_equal_distribution():

    result = allocate(500000)

    assert sum(result) == 500000

    assert len(result) == 5
