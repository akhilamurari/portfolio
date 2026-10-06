from app import app

def test_home():
    r = app.test_client().get("/")
    assert r.status_code == 200
    assert b"Akhila" in r.data

def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200