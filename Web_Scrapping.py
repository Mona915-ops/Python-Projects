import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_products(url):
    """Scrape product information from an e-commerce webpage."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    
    # This example is for scraping from Amazon; you may need to adjust the selectors for other websites.
    product_containers = soup.find_all("div", {"data-component-type": "s-search-result"})
    
    products = []
    for container in product_containers:
        # Extract product name
        name_tag = container.find("span", class_="a-size-medium")
        name = name_tag.text.strip() if name_tag else "N/A"

        # Extract price
        price_tag = container.find("span", class_="a-price-whole")
        price = price_tag.text.strip() if price_tag else "N/A"

        # Extract rating
        rating_tag = container.find("span", class_="a-icon-alt")
        rating = rating_tag.text.strip() if rating_tag else "N/A"

        products.append({"Name": name, "Price": price, "Rating": rating})
    
    return products

def save_to_csv(data, filename):
    """Save the scraped data to a CSV file."""
    if not data:
        print("No data to save.")
        return

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    # URL of the e-commerce page to scrape
    url = input("Enter the URL of the e-commerce webpage: ")
    scraped_data = scrape_products(url)
    
    # Save to CSV
    save_to_csv(scraped_data, "products.csv")
