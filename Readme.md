# Stock & News Alert App

This project is a **Streamlit** web app that monitors stock prices and sends news alerts when there’s a significant change in the stock price. The app pulls stock data from **Alpha Vantage** and news articles from **NewsAPI**. If a price change exceeds a certain threshold, the app fetches related news and automatically sends it as a notification via **Twilio**.

## Features

- Fetches daily stock data for the specified company.
- Calculates the price change percentage between the last two days.
- Retrieves relevant news articles if the stock price change exceeds a specified threshold.
- Sends news articles as notifications through Twilio if conditions are met.
- Easy-to-use web interface powered by Streamlit.

## Technologies Used

- **Python**
- **Streamlit** – For the front end
- **Alpha Vantage API** – For stock data
- **NewsAPI** – For news articles
- **Twilio API** – For sending SMS notifications

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
