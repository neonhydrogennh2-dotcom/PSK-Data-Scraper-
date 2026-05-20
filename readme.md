📈 PSX Market Pulse Scraper & Dashboard
A production-grade Python tool that extracts real-time market data from the Pakistan Stock Exchange (PSX), cleanses the data for financial analysis, and visualizes it through an interactive dashboard.

🚀 Features
Automated Extraction: Bypasses front-end JavaScript rendering by intercepting internal API endpoints.

Data Pipeline: Cleans and formats raw strings into specialized Python types (Floats, Integers).

Multi-Category Support: Captures Top Active Stocks, Top Advancers, and Top Decliners in a single pass.

Interactive Dashboard: A Streamlit-based UI to filter and view market trends instantly.

Portable Storage: Exports structured data to psx_market_pulse.csv for use in Excel or PowerBI.

🛠️ Tech Stack
Python 3.x

BeautifulSoup4: For parsing internal HTML data streams.

Requests: For high-speed data fetching with custom Header rotation.

Streamlit: For the data visualization dashboard.

CSV: For persistent data storage.

🧠 Key Learnings
Intercepting XHR/Fetch: Learned that modern websites often load data via background requests. Bypassing the main URL to hit the data source directly is faster and more reliable.

Handling "NoneType" Errors: Mastered debugging BeautifulSoup when selectors fail due to dynamic content.

Data Sanitization: Implemented logic to handle messy financial strings (removing commas, splitting percentages, and handling currency symbols).

Reusable Logic: Developed a functional programming approach to parse multiple tables using a single, robust function.

📊 How to Run
Clone the repo.

Install requirements: pip install requests beautifulsoup4 streamlit

Run the scraper: python pskdatascraper.py

Launch the dashboard: streamlit run pskdash.py