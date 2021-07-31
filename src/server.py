from decimal import Decimal
from enum import Enum
from typing import Any

from fastapi import FastAPI, Form, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import RedirectResponse, HTMLResponse, Response
from fastapi.templating import Jinja2Templates

from src.logic import calculate_overall_cost, calculate_total

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class StatesEnum(str, Enum):
    UT = 'UT'
    NV = 'NV'
    TX = 'TX'
    AL = 'AL'
    CA = 'CA'


def round_decimal(number: Decimal, precision: int = 2) -> Decimal:
    return number.quantize(Decimal(10) ** -precision)


@app.get('/')
async def redirect_root() -> Response:
    return RedirectResponse('/index.html')


@app.get('/index.html', response_class=HTMLResponse)
async def calculate_get(request: Request) -> Response:
    return templates.TemplateResponse('/index.html', {'request': request})


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, _: Any) -> Response:
    context = {'request': request, 'error': 'Invalid input'}
    return templates.TemplateResponse('/index.html', context)


@app.post('/index.html', response_class=HTMLResponse)
async def calculate_post(request: Request,
                         quantity: int = Form(..., gt=0),
                         price: Decimal = Form(..., gt=0),
                         state: StatesEnum = Form(...)) -> Response:
    subtotal = await calculate_overall_cost(price, quantity)
    total = await calculate_total(subtotal, state)

    context = {
        'request': request,
        'quantity': quantity,
        'price': price,
        'state': state.value,
        'subtotal': round_decimal(subtotal),
        'total': round_decimal(total),
    }

    return templates.TemplateResponse('/index.html', context)
