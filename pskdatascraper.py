import requests 
from bs4 import BeautifulSoup
import csv 

url = "https://dps.psx.com.pk/performers"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

response = requests.get(url, headers=headers)

# Extracting the data
#print(response.status_code)
#print(response.text[:600])

soup = BeautifulSoup(response.text, "html.parser")

def extract_data(table_object):
    table = []

    for row in table_object.find_all("tr"):
        cols = row.find_all("td")

        if not cols:
            continue 
    
        symbol = cols[0].text.strip()
        price = float(cols[1].text.strip().replace(",", ""))
        change = cols[2].text.strip().split()[0]
        volume = int(cols[3].text.strip().replace(",", ""))
        
    
        row_dict = {
            "Symbol": symbol,
            "Price": price,
            "Change": change,
            "Volume": volume
        }
        
        table.append(row_dict)
        
    return table
    
all_tables = soup.find_all("table", class_="tbl")

top_active_stocks = extract_data(all_tables[0])
top_advancers = extract_data(all_tables[1])
top_decliners = extract_data(all_tables[2])
    
    
csv_file = "psx_data.csv"
try:
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Symbol", "Price", "Change", "Volume"])
    
        for stock in top_active_stocks:
            writer.writerow(["Top Active Stocks", stock["Symbol"], stock["Price"], stock["Change"], stock["Volume"]])
        for stock in top_advancers:
            writer.writerow(["Top Advancers", stock["Symbol"], stock["Price"], stock["Change"], stock["Volume"]])
        for stock in top_decliners:
            writer.writerow(["Top Decliners", stock["Symbol"], stock["Price"], stock["Change"], stock["Volume"]])

    print(f"Data has been written to {csv_file}")
except Exception as e:
    print(f"An error occurred while writing to the CSV file: {e}")


