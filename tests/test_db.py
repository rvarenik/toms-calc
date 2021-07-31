from decimal import Decimal

import pytest

from src.db import get_discount, get_state_tax


@pytest.mark.asyncio
async def test_get_discount():
    assert await get_discount(Decimal(0)) == Decimal(0)
    assert await get_discount(Decimal(999)) == Decimal(0)
    assert await get_discount(Decimal(1000)) == Decimal('.03')
    assert await get_discount(Decimal(1001)) == Decimal('.03')
    assert await get_discount(Decimal(5000)) == Decimal('.05')
    assert await get_discount(Decimal(7000)) == Decimal('.07')
    assert await get_discount(Decimal(10000)) == Decimal('.1')
    assert await get_discount(Decimal(50000)) == Decimal('.15')


@pytest.mark.asyncio
async def test_get_discount_invalid():
    with pytest.raises(KeyError):
        await get_discount(Decimal(-1))


@pytest.mark.asyncio
async def test_get_state_tax_invalid():
    with pytest.raises(KeyError):
        await get_state_tax('QQ')


@pytest.mark.asyncio
async def test_get_state_tax():
    assert await get_state_tax('NV') == Decimal('.08')
    assert await get_state_tax('TX') == Decimal('.0625')
