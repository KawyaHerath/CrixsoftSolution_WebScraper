"""
Web Scraper - Crixsoft Solution Internship Project 1
-------------------------------------------------------
Scrapes quotes (text, author, tags) from http://quotes.toscrape.com
(a public site built specifically for scraping practice) and saves
the data in structured CSV and JSON formats.

Requirements:
    pip install requests beautifulsoup4

Usage:
    python web_scraper.py
    python web_scraper.py --pages 3 --output my_quotes
"""

import argparse
import csv
import json
import sys
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://quotes.toscrape.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (CrixsoftSolutionScraper/1.0)"}


def fetch_page(url):
    """Fetch a single page and return a BeautifulSoup object, or None on failure."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as exc:
        print(f"  [!] Failed to fetch {url}: {exc}")
        return None


def parse_quotes(soup):
    """Extract quote text, author, and tags from a page's soup object."""
    records = []
    for block in soup.select(".quote"):
        text = block.select_one(".text").get_text(strip=True).strip('“”"')
        author = block.select_one(".author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in block.select(".tags .tag")]
        records.append({"quote": text, "author": author, "tags": ", ".join(tags)})
    return records


def get_next_page_url(soup):
    next_btn = soup.select_one(".next > a")
    if next_btn and next_btn.get("href"):
        return BASE_URL + next_btn["href"]
    return None


def scrape(max_pages=None):
    """Scrape quotes across pages, following the 'Next' link until done."""
    all_records = []
    url = BASE_URL
    page_num = 1

    while url:
        print(f"Scraping page {page_num}: {url}")
        soup = fetch_page(url)
        if soup is None:
            break

        records = parse_quotes(soup)
        all_records.extend(records)
        print(f"  -> Found {len(records)} quotes (total so far: {len(all_records)})")

        if max_pages and page_num >= max_pages:
            break

        url = get_next_page_url(soup)
        page_num += 1
        time.sleep(0.5)  # be polite to the server

    return all_records


def save_csv(records, filename):
    if not records:
        print("No records to save.")
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)
    print(f"Saved {len(records)} records to {filename}")


def save_json(records, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(records)} records to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Scrape quotes from quotes.toscrape.com")
    parser.add_argument("--pages", type=int, default=None,
                         help="Maximum number of pages to scrape (default: all pages)")
    parser.add_argument("--output", type=str, default="quotes",
                         help="Base filename for output (without extension)")
    args = parser.parse_args()

    print("=== Crixsoft Solution - Web Scraper ===\n")
    records = scrape(max_pages=args.pages)

    if not records:
        print("No data scraped. Exiting.")
        sys.exit(1)

    save_csv(records, f"{args.output}.csv")
    save_json(records, f"{args.output}.json")
    print(f"\nDone! Scraped a total of {len(records)} quotes.")


if __name__ == "__main__":
    main()
