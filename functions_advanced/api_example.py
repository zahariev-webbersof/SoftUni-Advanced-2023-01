import requests

# API endpoint
url = 'http://newsapi.org/v2/top-headlines?country=us&apiKey=21b97a2792e3468d811f48ad28201c38'

# Make request to the API
response = requests.get(url)

# Get the response data as a python object
news_data = response.json()

articles_counter = 1

print(news_data)

# for article in news_data['articles']:
#     if articles_counter <= 5:
#         print(f"{articles_counter}: {article['title']}")
#         articles_counter += 1
#     else:
#         break