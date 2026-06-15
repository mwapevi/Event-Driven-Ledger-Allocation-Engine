from app.services.allocation_engine \
import calculate_allocations

def test_allocations():

    result = calculate_allocations(
        1000
    )

    assert result["profit"] == 50
    assert result["ownerpay"] == 500
    assert result["tax"] == 150
    assert result["opex"] == 250
    assert result["growth"] == 50