import requests
from bs4 import BeautifulSoup
import csv

def scrape_example():
    # Target website (replace with any public site you want to scrape)
    url = "https://quotes.toscrape.com/"
    
    # Send HTTP request
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code != 200:
        print("⚠️ Failed to retrieve the webpage.")
        return
    
    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract relevant data (quotes and authors)
    quotes_data = []
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    
    for quote, author in zip(quotes, authors):
        quotes_data.append([quote.get_text(), author.get_text()])
    
    # Save data to CSV file
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])  # Header row
        writer.writerows(quotes_data)
    
    print("✅ Data scraped and saved to quotes.csv")

# Entry point
if __name__ == "__main__":
    scrape_example()