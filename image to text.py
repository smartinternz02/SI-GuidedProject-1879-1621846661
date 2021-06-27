import requests

url = "https://unfound-text-summarization-v1.p.rapidapi.com/summarization"

payload = "{\n    \"input_data\": \"https://www.tesla.com/elon-musk\",\n    \"input_type\": \"url\",\n    \"summary_type\": \"general_summary\",\n    \"N\": 3\n}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    'x-rapidapi-host': "unfound-text-summarization-v1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
