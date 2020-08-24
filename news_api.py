import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'q=Hydrogen&'
       'from=2020-08-17&'
       'sortBy=popularity&'
       'apiKey=3e6a3a7a4a62409f8dc472abb47a95a5')
response = requests.get(url)
print(response.json())
