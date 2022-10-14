import requests

response = requests.get(url="https://opentdb.com/api.php", params={"amount": 10, "type": "boolean"})
question_data = response.json()["results"]