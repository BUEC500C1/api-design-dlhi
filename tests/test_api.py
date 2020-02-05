import sys

sys.path.append('./src')


def test_server():
    from api import app
    temp_client = app.test_client()
    data = temp_client.get('/airportInfo?gpscode=KBOS')
    assert data._status_code == 200


def test_server_missing_input():
    from api import app
    temp_client = app.test_client()
    data = temp_client.get('/airportInfo')
    assert data._status_code != 200
