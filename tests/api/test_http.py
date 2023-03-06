import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('http://api.github.com/zen')
    print(f'Response is {r.text}')


@pytest.mark.http
def test_second_request():
    r = requests.get('http://api.github.com/users/dblidchenko')
    body = r.json()  # json() - method, виводимо тіло відповіді
    headers = r.headers

    assert body['name'] == 'Dmytro Blidchenko'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    r = requests.get('http://api.github.com/users/dmytro_blidchenko')

    assert r.status_code == 404
