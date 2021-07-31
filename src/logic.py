from decimal import Decimal

from .db import get_discount, get_state_tax


async def calculate_overall_cost(price: Decimal, qty: int) -> Decimal:
    if price <= 0:
        raise ValueError('invalid price')

    if qty <= 0:
        raise ValueError('invalid quantity')

    overall_cost = price * qty
    overall_cost -= overall_cost * await get_discount(overall_cost)
    return overall_cost


async def calculate_total(subtotal: Decimal, state: str) -> Decimal:
    if subtotal <= 0:
        raise ValueError('invalid subtotal')

    tax = await get_state_tax(state)
    return subtotal + subtotal * tax
