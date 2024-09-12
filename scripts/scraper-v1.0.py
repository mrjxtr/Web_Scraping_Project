import logging
import os
import random
import time
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Referer": os.getenv("REFERER_URL"),  # REFERER_URL from .env file
    "DNT": "1",  # Do Not Track Request Header
}


def fetch_charity_data(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Failed to load page {url}: {e}")
        raise
    return response.content


def parse_charity_data(html_content, base_url):
    soup = BeautifulSoup(html_content, "html.parser")
    charity_list = []

    # Find all span elements with the class 'largePara'
    charity_spans = soup.find_all("span", class_="largePara")
    if not charity_spans:
        logging.error("Failed to find the charity section")
        # Print the HTML content for debugging
        logging.debug(soup.prettify())
        raise Exception("Failed to find the charity section")

    # Extract charity names and URLs
    for span in charity_spans:
        link = span.find("a", href=True)
        if link:
            charity_name = link.text.strip()
            charity_url = urljoin(base_url, link["href"])
            charity_list.append((charity_name, charity_url))

    return charity_list


def find_letter_urls(soup, base_url):
    letter_urls = []
    letter_links = soup.select("span.largePara a")
    for link in letter_links:
        letter_url = urljoin(base_url, link["href"])
        letter_urls.append(letter_url)
    return letter_urls


def save_to_csv(charity_list, filename):
    df = pd.DataFrame(charity_list, columns=["Charity Name", "URL"])
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    logging.info(f"Saved {len(charity_list)} charities to {filename}")


def main():
    base_url = os.getenv("BASE_URL")  # BASE_URL from .env file
    url = base_url
    all_charities = []

    try:
        # Fetch the main page to get the letter URLs
        html_content = fetch_charity_data(url)
        soup = BeautifulSoup(html_content, "html.parser")
        letter_urls = find_letter_urls(soup, base_url)

        # Iterate through each letter URL
        for letter_url in letter_urls:
            try:
                html_content = fetch_charity_data(letter_url)
                time.sleep(random.uniform(1, 8))
                charity_list = parse_charity_data(html_content, base_url)
                time.sleep(random.uniform(1, 5))
                all_charities.extend(charity_list)
            except Exception as e:
                logging.error(f"An error occurred while processing {letter_url}: {e}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path
    csv_path = os.path.join(script_dir, "../data/raw/charities_list.csv")

    save_to_csv(all_charities, csv_path)


if __name__ == "__main__":
    main()
