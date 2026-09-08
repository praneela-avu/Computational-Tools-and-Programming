import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

BASE_URL = "https://books.toscrape.com/"
OUTPUT_FILE = "books.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_page(url):
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    # Each book is inside an <article class="product_pod">
    for book in soup.select("article.product_pod"):

        # Book title
        title_tag = book.select_one("h3 a")
        title = title_tag.get("title", "") if title_tag else ""

        # Price
        price_tag = book.select_one(".price_color")
        price = price_tag.get_text(strip=True) if price_tag else ""

        # Rating
        rating_tag = book.select_one("p.star-rating")
        rating = ""

        if rating_tag:
            rating_classes = rating_tag.get("class", [])
            if len(rating_classes) > 1:
                rating = rating_classes[1]

        # Availability
        availability_tag = book.select_one(".availability")
        availability = (
            availability_tag.get_text(" ", strip=True)
            if availability_tag
            else ""
        )

        # Product URL
        link_tag = book.select_one("h3 a")
        product_url = ""

        if link_tag and link_tag.get("href"):
            product_url = urljoin(url, link_tag["href"])

        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
            "url": product_url
        })

    return books


def save_to_csv(books):
    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "title",
            "price",
            "rating",
            "availability",
            "url"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(books)


def main():

    all_books = []

    # Books to Scrape has 50 pages
    for page in range(1, 51):

        if page == 1:
            url = BASE_URL
        else:
            url = f"{BASE_URL}catalogue/page-{page}.html"

        print(f"Scraping page {page}: {url}")

        try:
            books = scrape_page(url)

            print(f"  Found {len(books)} books")

            all_books.extend(books)

            # Be polite to the server
            time.sleep(1)

        except requests.RequestException as error:
            print(f"  Error: {error}")

    save_to_csv(all_books)

    print()
    print(f"Finished!")
    print(f"Total books scraped: {len(all_books)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
