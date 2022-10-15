import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_KEY = "key"
NEWSAPI_KEY = "key"

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
stock_response = requests.get(url=url,
                              params={"function": "TIME_SERIES_DAILY",
                                      "symbol": "TSLA",
                                      "outputsize": "compact",
                                      "apikey": ALPHAVANTAGE_KEY})
stock_data = stock_response.json()["Time Series (Daily)"]
today_yesterday = [value for (key, value) in stock_data.items()][:2]
difference = float(today_yesterday[0]["4. close"]) - float(today_yesterday[1]["4. close"])
change = abs(difference) / float(today_yesterday[0]["4. close"]) * 100
if abs(difference) / float(today_yesterday[0]["4. close"]) > 0.05:
    if difference < 0:
        print(f"Stock price fell by {round(abs(difference), 2)} points, -{round(change, 2)}%")
    else:
        print(f"Stock price increased by {round(abs(difference), 2)} points, +{round(change, 2)}%")

newsresponse = requests.get(url="https://newsapi.org/v2/everything",
                            params={"q": COMPANY_NAME,
                                    "apiKey": NEWSAPI_KEY})
articles = newsresponse.json()["articles"][:3]
articles_list = [f"Headline: {article['title']}.\nDescription: {article['description']}" for article in articles]
print(articles_list)
