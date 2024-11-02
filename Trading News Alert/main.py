import streamlit as st
import requests
from twilio.rest import Client

# API Endpoints and Configuration
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'

STOCK_API_KEY = "KHTB4AISFLTSB2XF"
NEWS_API_KEY = "171cdd0cda2b459a8d7b4aba35a35a20"
TWILIO_SID = "ACb1a3912611ed522f76bc323745dfc856"
TWILIO_AUTH_TOKEN = "5c6eaffc90b8876fa9271b93c56b049a"

def get_stock_data():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()['Time Series (Daily)']
    return [value for (key, value) in data.items()]

def get_news():
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    new_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = new_response.json().get('articles', [])
    return articles[:3]  # Get top 3 articles

def send_notification(article_text):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=article_text,
        from_="+12177182567",
        to="+919568440014"
    )

# Streamlit Layout
st.title("Stock & News Alert App")
st.subheader(f"Stock Name: {STOCK_NAME}")
st.write(f"Company: {COMPANY_NAME}")

# Display Stock Price Difference
data_list = get_stock_data()
yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]

yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
difference_percentage = (difference / yesterday_closing_price) * 100

st.metric("Yesterday's Closing Price", f"${yesterday_closing_price}")
st.metric("Day Before Yesterday's Closing Price", f"${day_before_yesterday_closing_price}")
st.metric("Price Difference (%)", f"{difference_percentage:.2f}%")

# Check if Price Difference Exceeds Threshold and Send Notifications Automatically
if difference_percentage > 0.1:
    st.warning("Significant price change detected! Fetching news and sending notification...")

    articles = get_news()
    
    for article in articles:
        st.subheader(article['title'])
        st.write(article['description'])
        
        # Automatically send notification for each article
        article_text = f"Headline: {article['title']}\nBrief: {article['description']}"
        send_notification(article_text)

    st.success("Notifications sent to your mobile number!")
else:
    st.info("No significant price change. No news available.")


