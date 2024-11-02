from src.app import app

def test_home():
    assert app.test_client().get("/").status_code == 200
    assert app.test_client().get("/").data == b"HELLO WORLD"
    