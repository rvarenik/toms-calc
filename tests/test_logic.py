from decimal import Decimal

import pytest

from src.logic import calculate_overall_cost, calculate_total


@pytest.mark.asyncio
async def test_calculate_overall_cost_invalid():
    with pytest.raises(ValueError):
        await calculate_overall_cost(Decimal(-2), 42)
        await calculate_overall_cost(Decimal(0), 42)
        await calculate_overall_cost(Decimal(42), -5)
        await calculate_overall_cost(Decimal(42), 0)


@pytest.mark.asyncio
async def test_calculate_overall_cost():
    assert await calculate_overall_cost(Decimal('18.45'), 1) == Decimal('18.45')
    assert await calculate_overall_cost(Decimal('18.45'), 6) == Decimal('110.7')
    assert await calculate_overall_cost(Decimal('1000'), 2) == Decimal('1940')
    assert await calculate_overall_cost(Decimal('2000'), 5) == Decimal('9000')


@pytest.mark.asyncio
async def test_calculate_total_invalid():
    with pytest.raises(ValueError):
        await calculate_total(Decimal(-2), 'TX')
        await calculate_total(Decimal(0), 'TX')


@pytest.mark.asyncio
async def test_calculate_total():
    assert await calculate_total(Decimal('18.45'), 'AL') == Decimal('19.188')
    assert await calculate_total(Decimal('1000'), 'UT') == Decimal('1068.5')
    assert await calculate_total(Decimal('1.25'), 'UT') == Decimal('1.335625')
