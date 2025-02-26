import requests

def fetch_data():
    """
    Demonstration function that uses the old (and potentially vulnerable)
    'requests==2.19.1' to fetch data from a public API.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()

