import requests


def fetch_text(url):
    if not (type(url) is str and url.startswith("http")):
        raise ValueError
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e: 
        raise e
