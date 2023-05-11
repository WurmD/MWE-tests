from src.main import create_str


def test_string_produced():
    string = create_str()
    assert string == "Hello World!"
