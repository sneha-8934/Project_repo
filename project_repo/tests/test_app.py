from src.app import greet

def test_greet():
    assert greet("Jim") == "Hello, Jim!"
