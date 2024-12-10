import pytest
from src.utils.utils import fetch_text

@pytest.mark.parametrize("url, expected", [
    ("http://example.com", "Example Domain"),
    ("http://google.com", "Google")
])
def test_fetch_test(url, expected):
    assert expected in fetch_text(url)


@pytest.mark.parametrize("url, error", [
    ("not_url", ValueError),
    (12, ValueError),
    ("https://fake-url.net", Exception)
])
def test_fail_fetch_text(url, error):
    with pytest.raises(error):
        fetch_text(url)