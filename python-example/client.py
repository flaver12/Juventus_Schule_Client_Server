import requests

# url that we want to fetch
api_url = "https://jsonplaceholder.typicode.com/todos/1"

# make the request
response = requests.get(api_url)

# convert to json
json = response.json()

# print it out
print(json)
