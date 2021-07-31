from decimal import Decimal

Discounts = {
    1000: 3,
    5000: 5,
    7000: 7,
    10000: 10,
    50000: 15,
}

Taxes = {
    'UT': '6.85',
    'NV': '8',
    'TX': '6.25',
    'AL': '4',
    'CA': '8.25',
}


async def get_discount(sum_: Decimal) -> Decimal:
    if sum_ < Decimal():
        raise KeyError('negative value')

    discount = 0
    for s, d in Discounts.items():
        if sum_ >= s:
            discount = d
        else:
            break
    return Decimal(discount) / 100


async def get_state_tax(state: str) -> Decimal:
    return Decimal(Taxes[state]) / 100
