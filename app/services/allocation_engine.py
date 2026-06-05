def allocate(amount: int):

    share = amount // 5

    allocations = [
        share,
        share,
        share,
        share,
        share,
    ]

    remainder = amount - sum(allocations)

    allocations[0] += remainder

    return allocations
