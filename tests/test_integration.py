from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_start_page():
    response = client.get('/')
    assert response.status_code == 200
    assert response.template.name == '/index.html'
    assert not all(c in response.context for c in ['error', 'quantity', 'price', 'state', 'subtotal', 'total'])


def test_error():
    response = client.post('/index.html', data={})
    assert response.status_code == 200
    assert response.template.name == '/index.html'
    assert 'error' in response.context

    response = client.post('/index.html', data={'state': 'ZZ'})
    assert response.status_code == 200
    assert 'error' in response.context


def test_calculator_1():
    data = {'price': '42', 'quantity': 100, 'state': 'AL'}
    response = client.post('/index.html', data=data)
    assert response.status_code == 200
    assert response.template.name == '/index.html'
    assert 'error' not in response.context
    assert str(response.context['quantity']) == '100'
    assert str(response.context['price']) == '42'
    assert str(response.context['state']) == 'AL'
    assert str(response.context['subtotal']) == '4074.00'
    assert str(response.context['total']) == '4236.96'


def test_calculator_2():
    data = {'price': '42', 'quantity': 99, 'state': 'UT'}
    response = client.post('/index.html', data=data)
    assert response.status_code == 200
    assert response.template.name == '/index.html'
    assert 'error' not in response.context
    assert str(response.context['quantity']) == '99'
    assert str(response.context['price']) == '42'
    assert str(response.context['state']) == 'UT'
    assert str(response.context['subtotal']) == '4033.26'
    assert str(response.context['total']) == '4309.54'
