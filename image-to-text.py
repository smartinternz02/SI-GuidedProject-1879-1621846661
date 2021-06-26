import requests

url = "https://image-to-text2.p.rapidapi.com/cloudVision/imageToText"

querystring = {"source":"https://images.unsplash.com/photo-1564164460286-bf52d8a6ee09?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1870&q=80","sourceType":"url"}

payload = "{\r\n    \"source\": \"https://images.unsplash.com/photo-1564164460286-bf52d8a6ee09?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1870&q=80\",\r\n    \"sourceType\": \"url\"\r\n}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "16e898c974msh2e2909ad9b5fd62p1f8800jsn67462d368073",
    'x-rapidapi-host': "image-to-text2.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
