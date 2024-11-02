Stock & News Alert App
This project is a Streamlit web app that monitors stock prices and sends news alerts when there’s a significant change in the stock price. The app pulls stock data from Alpha Vantage and news articles from NewsAPI. If a price change exceeds a certain threshold, the app fetches related news and automatically sends it as a notification via Twilio.

Features
Fetches daily stock data for the specified company.
Calculates the price change percentage between the last two days.
Retrieves relevant news articles if the stock price change exceeds a specified threshold.
Sends news articles as notifications through Twilio if conditions are met.
Easy-to-use web interface powered by Streamlit.
Technologies Used
Python
Streamlit – For the front end
Alpha Vantage API – For stock data
NewsAPI – For news articles
Twilio API – For sending SMS notifications
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

In your project directory, create a file named .env and add your API keys and other sensitive information:

plaintext
Copy code
STOCK_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_news_api_key
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
RECIPIENT_PHONE_NUMBER=recipient_phone_number
Alternatively, if deploying on Streamlit Community Cloud, set the above variables in the Secrets section of the app's settings.

Running the App Locally
Run the following command in your project directory to start the app:

bash
Copy code
streamlit run app.py
Deploying the App on Streamlit Community Cloud
Push your code to a GitHub repository.
Go to Streamlit Community Cloud and log in.
Click on "New app", select your repository, branch, and app.py file.
Set the required environment variables under Secrets in your app's settings:
STOCK_API_KEY
NEWS_API_KEY
TWILIO_SID
TWILIO_AUTH_TOKEN
TWILIO_PHONE_NUMBER
RECIPIENT_PHONE_NUMBER
Click Deploy.
Once deployed, you can access your app via the unique URL provided by Streamlit.

Usage
The app displays stock price data and calculates the percentage change.
If the price change exceeds a specified threshold (5% by default), it automatically fetches news related to the stock's company.
Relevant news articles are sent to your phone via Twilio SMS.
Customization
Threshold for Notifications: Adjust the threshold in app.py by modifying this line:
python
Copy code
if difference_percentage > 5:
Target Stock: Change the STOCK_NAME and COMPANY_NAME variables in app.py to monitor a different stock.
