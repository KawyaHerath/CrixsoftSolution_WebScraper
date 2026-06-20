# Crixsoft Solution – Web Scraper Project

📌 **Internship Project 1 | Python Development**
🏢 Completed as part of the **Crixsoft Solution** Python Development Internship.

## 📖 About

A Python web scraper that extracts quotes, authors, and tags from
[quotes.toscrape.com](http://quotes.toscrape.com) — a site built specifically
for scraping practice — and saves the results in structured **CSV** and
**JSON** formats. The scraper automatically follows pagination to collect
data across all available pages.

## ✨ Features

- Scrapes quote text, author name, and tags from every page
- Automatically follows "Next" pagination links
- Saves output to both `.csv` and `.json`
- Command-line arguments to limit pages or set a custom output filename
- Polite scraping with request delays and proper error handling

## 🛠️ Tech Stack

- Python 3
- [Requests](https://docs.python-requests.org/) – HTTP requests
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/CrixsoftSolution_WebScraper.git
cd CrixsoftSolution_WebScraper
pip install -r requirements.txt
```

## ▶️ Usage

Scrape all pages (default):

```bash
python web_scraper.py
```

Scrape only the first 3 pages, with a custom output filename:

```bash
python web_scraper.py --pages 3 --output my_quotes
```

This generates `my_quotes.csv` and `my_quotes.json` in the project folder.

## 📂 Sample Output (JSON)

```json
[
  {
    "quote": "The world as we have created it is a process of our thinking...",
    "author": "Albert Einstein",
    "tags": "change, deep-thoughts, thinking, world"
  }
]
```

## 🎯 What I Learned

- Parsing HTML with BeautifulSoup selectors
- Handling pagination in web scraping
- Structuring and exporting scraped data (CSV/JSON)
- Writing resilient code with error handling for failed requests

## 👤 Author

Built as part of the **Crixsoft Solution** internship program.
🔗 [Crixsoft Solution on LinkedIn](https://www.linkedin.com/company/crixsoft-solution)
